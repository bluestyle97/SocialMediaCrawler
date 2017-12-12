"""
@author : Jiale Xu
@date: 2017/11/11
@desc: Search zhihu users and get html.
"""
import re
from urllib.request import quote

import requests
from bs4 import BeautifulSoup

from lib.configs import zhihu_search_url, zhihu_header


def get_user_by_search(user, number=1, start=0):
    assert isinstance(number, int), 'Parameter \'number\' isn\'t an instance of type \'int\'!'
    assert isinstance(start, int), 'Parameter \'start\' isn\'t an instance of type \'int\'!'
    assert number >= 1, 'Parameter \'number\' is smaller than 1!'

    position = start
    response = requests.get(zhihu_search_url.format(key=quote(user), offset=position),
                            headers=zhihu_header)
    result = response.json()
    user_tokens = []
    user_htmls = []
    while len(user_tokens) < number:
        for html in result.get('htmls'):
            bs = BeautifulSoup(html, 'lxml')
            user_tokens.append(bs.li.attrs['data-token'])
            user_htmls.append(bs.li.prettify())
        if len(result.get('htmls')) < 10:
            break
        if len(user_tokens) < number:
            position += 10
            response = requests.get(zhihu_search_url.format(key=quote(user), offset=position),
                                    headers=zhihu_header)
            result = response.json()
    if len(user_tokens) > number:
        user_tokens = user_tokens[:number]
        user_htmls = user_htmls[:number]
    return user_tokens, user_htmls


def get_user_by_homepage(url):
    assert isinstance(url, str), 'Parameter \'url\' must be an instance of \'str\'!'

    if not re.match(r'https://www\.zhihu\.com/people/.*', url):  # 不合法的主页地址
        return None, None
    user = re.search(r'https://www\.zhihu\.com/people/(.*)', url).group(1).split('/')[0]
    response = requests.get('https://www.zhihu.com/people/' + user + '/activities',
                            headers=zhihu_header)
    if response.status_code == 404:  # 用户不存在
        return None, None
    bs = BeautifulSoup(response.text, 'lxml')
    user_name = bs.find('span', {'class': 'ProfileHeader-name'}).get_text()
    start = 0
    while True:
        user_tokens, user_htmls = get_user_by_search(user=user_name, number=10, start=start)
        if len(user_tokens) == 0:
            break
        for user_token, user_html in zip(user_tokens, user_htmls):
            if re.search(r'data-token=\"(.*?)\"', str(user_html)).group(1) == user:
                return user_token, user_html
        start += 10
    return None, None


if __name__ == '__main__':
    print(get_user_by_homepage('https://www.zhihu.com/people/jiang-feng-72-58/activities'))
    print(get_user_by_search('江枫', 10))
