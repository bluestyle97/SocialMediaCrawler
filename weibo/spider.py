"""
weibo.spider
~~~~~~~~~~~~

This module implements the spider of sina weibo.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/10/05.
:license: MIT License, see LICENSE.txt for more details.
"""
import datetime
import logging
import re
import time
import os
import requests
from lib.basis import Sex, SocialMediaSpider
from lib.configs import weibo_user_follower_url, weibo_user_following_url, weibo_user_info_url, \
    weibo_user_homepage_url, weibo_user_weibo_url
from weibo.items import WeiboUserItem, WeiboContentItem, WeiboRepostContentItem


class WeiboSpider(SocialMediaSpider):
    def __init__(self, log=False, log_dir=''):
        """
        :param log: if True, save logs while scraping; if False, don't save.
        :param log_dir: directory of log files, only available when `log` is True.
        """
        assert isinstance(log, bool), 'Parameter \'log\' should be an instance of type \'bool\'. ' \
                                      'Found: %s.' % type(log)

        # If `log` is True, then configure available path in order to save log files.
        if log:
            self._log = True
            if not isinstance(log_dir, str):
                raise TypeError('Parameter \'log_path\' should be a instance of type \'str\'. '
                                'Found: %s.' % type(log_dir))
            else:
                if not os.path.exists(log_dir):
                    if not os.path.exists(os.getcwd() + '/logs'):
                        os.mkdir(os.getcwd() + '/logs')
                    log_dir = os.getcwd() + '/logs'
            log_file = log_dir + '/weibo-log-%s.log' % (datetime.date.today())
            logging.basicConfig(
                filename=log_file,
                format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                level=10)
        # If `log` is False, do nothing.
        else:
            self._log = False

        self.scraped_infos = {}
        self.scraped_follows = {}
        self.scraped_fans = {}
        self.scraped_weibos = {}

    def scrape_user_info(self, id):
        assert isinstance(id, int), 'Parameter \'id\' should be an instance of type \'int\'!'
        assert id > 0, 'Parameter \'id\' should be positive!'

        if self._log:
            logging.info('Scraping info of weibo user: %d...' % id)
        item = WeiboUserItem()
        item.id = id
        item.link = 'https://weibo.com/u/{uid}'.format(uid=id)

        # 通过主页请求获取关注数、粉丝数、头像url
        response = requests.get(weibo_user_homepage_url.format(uid1=id, uid2=id))
        result = response.json()
        item.following_count = result.get('data').get('userInfo').get('follow_count')
        item.follower_count = result.get('data').get('userInfo').get('followers_count')
        item.avatar = result.get('data').get('userInfo').get('profile_image_url')

        # 通过详细资料请求获取详细资料
        response = requests.get(weibo_user_info_url.format(uid1=id, uid2=id))
        result = response.json()
        for card in result.get('data').get('cards'):
            if card.get('card_type') != 11:
                continue
            for card_inner in card.get('card_group'):
                if card_inner.get('card_type') != 41:
                    continue
                item_name = card_inner.get('item_name')
                item_content = card_inner.get('item_content')
                if item_name == '昵称':
                    item.name = item_content
                elif item_name == '性别':
                    item.sex = Sex.MALE if item_content == '男' else Sex.FEMALE
                elif item_name == '所在地':
                    item.location = item_content
                elif item_name == '简介':
                    item.description = item_content
                elif item_name == '注册时间':
                    item.signup_time = item_content

        # 通过用户微博请求获取用户微博数
        response = requests.get(weibo_user_weibo_url.format(uid1=id, uid2=id, page=1))
        result = response.json()
        item.weibo_count = result.get('data').get('cardlistInfo').get('total')
        if self._log:
            logging.info('Succeed in scraping info of weibo user: %d.' % id)
        self.scraped_infos[id] = item
        return item

    def scrape_user_following(self, id, number=1):
        assert isinstance(id, int), 'Parameter \'id\' should be an instance of type \'int\'!'
        assert isinstance(number,
                          int), 'Parameter \'number\' should be an instance of type \'int\'!'
        assert number >= 1, 'Parameter \'number\' should be bigger than 1!'

        if self._log:
            logging.info('Scraping follows of weibo user: %d...' % id)
        response = requests.get(weibo_user_following_url.format(uid=id, page=1))
        result = response.json()
        total = result.get('data').get('count')
        number = min((number, total))
        followings = []
        position = 0
        while len(followings) < number:
            position += 1
            response = requests.get(weibo_user_following_url.format(uid=id, page=position))
            result = response.json()
            for card in result.get('data').get('cards'):
                user = card.get('user')
                item = WeiboUserItem()
                item.id = user.get('id')
                item.name = user.get('screen_name')
                item.link = 'https://weibo.com/u/{uid}'.format(uid=item.id)
                item.sex = Sex.MALE if user.get('gender') == 'm' else Sex.FEMALE
                item.avatar = user.get('profile_image_url')
                item.description = user.get('description')
                item.weibo_count = user.get('statuses_count')
                item.following_count = user.get('follow_count')
                item.follower_count = user.get('followers_count')
                response_info = requests.get(weibo_user_info_url.format(uid1=item.id, uid2=item.id))
                result_info = response_info.json()
                for card in result_info.get('data').get('cards'):
                    if card.get('card_type') != 11:
                        continue
                    for card_inner in card.get('card_group'):
                        if card_inner.get('card_type') != 41:
                            continue
                        item_name = card_inner.get('item_name')
                        item_content = card_inner.get('item_content')
                        if item_name == '所在地':
                            item.location = item_content
                        elif item_name == '注册时间':
                            item.signup_time = item_content
                followings.append(item)
                if len(followings) >= number:
                    break
        if self._log:
            logging.info('Succeed in scraping follows of weibo user: %d.' % id)
        self.scraped_follows[id] = followings
        return followings

    def scrape_user_follower(self, id, number=1):
        assert isinstance(id, int), 'Parameter \'id\' should be an instance of type \'int\'!'
        assert isinstance(number,
                          int), 'Parameter \'number\' should be an instance of type \'int\'!'
        assert number >= 1, 'Parameter \'number\' should be bigger than 1!'

        if self._log:
            logging.info('Scraping fans of weibo user: %d...' % id)
        response = requests.get(weibo_user_follower_url.format(uid=id, page=1))
        result = response.json()
        total = result.get('data').get('count')
        number = min((number, total))
        followers = []
        position = 0
        while len(followers) < number:
            position += 1
            response = requests.get(weibo_user_follower_url.format(uid=id, page=position))
            result = response.json()
            for card in result.get('data').get('cards'):
                user = card.get('user')
                item = WeiboUserItem()
                item.id = user.get('id')
                item.name = user.get('screen_name')
                item.link = 'https://weibo.com/u/{uid}'.format(uid=item.id)
                item.sex = Sex.MALE if user.get('gender') == 'm' else Sex.FEMALE
                item.avatar = user.get('profile_image_url')
                item.description = user.get('description')
                item.weibo_count = user.get('statuses_count')
                item.following_count = user.get('follow_count')
                item.follower_count = user.get('followers_count')
                response_info = requests.get(weibo_user_info_url.format(uid1=item.id, uid2=item.id))
                result_info = response_info.json()
                for card in result_info.get('data').get('cards'):
                    if card.get('card_type') != 11:
                        continue
                    for card_inner in card.get('card_group'):
                        if card_inner.get('card_type') != 41:
                            continue
                        item_name = card_inner.get('item_name')
                        item_content = card_inner.get('item_content')
                        if item_name == '所在地':
                            item.location = item_content
                        elif item_name == '注册时间':
                            item.signup_time = item_content
                followers.append(item)
                if len(followers) >= number:
                    break
        if self._log:
            logging.info('Succeed in scraping follows of weibo user: %d.' % id)
        self.scraped_fans[id] = followers
        return followers

    def scrape_user_weibo(self, id, before=None, after=None, number=1):
        assert isinstance(id, int), 'Parameter \'id\' should be an instance of type \'int\'!'
        assert isinstance(number,
                          int), 'Parameter \'number\' should be an instance of type \'int\'!'
        assert number >= 1, 'Parameter \'number\' should be bigger than 1!'

        before = int(time.time()) if before is None else int(before)
        after = 0 if after is None else int(after)
        if self._log:
            logging.info('Scraping weibos of weibo user: %d...' % id)
        response = requests.get(weibo_user_weibo_url.format(uid1=id, uid2=id, page=1))
        result = response.json()
        total = result.get('data').get('cardlistInfo').get('total')
        number = min((number, total))
        weibos = []
        position = 0
        stop_flag = False
        while len(weibos) < number:
            position += 1
            response = requests.get(weibo_user_weibo_url.format(uid1=id, uid2=id, page=position))
            result = response.json()
            for card in result.get('data').get('cards'):
                if card.get('card_type') != 9:
                    continue
                res = requests.get(card.get('scheme'))
                if '微博-出错了' in res.text:  # 该微博已被删除
                    continue
                time_lst = re.search(r'"created_at": "(.*?)"', res.text).group(1).split()
                time_lst.pop(-2)  # 删除时区信息
                time_str = ' '.join(time_lst)
                time_value = time.mktime(time.strptime(time_str, '%a %b %d %H:%M:%S %Y'))  # 获取时间戳
                mblog = card.get('mblog')
                if time_value > before:
                    continue
                if time_value < after:
                    if not mblog.get('isTop'):  # 置顶微博有可能造成异常
                        stop_flag = True
                        break
                    else:
                        continue
                if 'retweeted_status' in mblog.keys():  # 转发微博
                    item = WeiboRepostContentItem()
                    retweet = mblog.get('retweeted_status')
                    item.content = retweet.get('text')
                    item.source_id = retweet.get('bid')
                    if 'pics' in retweet.keys():
                        for pic in retweet.get('pics'):
                            item.pictures.append(pic.get('url'))
                    if 'page_info' in retweet.keys():
                        page_url = retweet.get('page_info').get('page_url')
                        if re.match(r'http://media\.weibo\.cn/article\?.*id=\d+',
                                    page_url):  # 移动端文章链接打不开，将其换为PC端链接
                            article_id = re.search(r'http://media\.weibo\.cn/article\?.*id=(\d+)',
                                                   page_url).group(1)
                            item.media = 'https://weibo.com/ttarticle/p/show?id={id}'.format(
                                id=article_id)
                        else:
                            item.media = page_url
                    if retweet.get('user') is not None:  # 原微博可能已被删除
                        item.source_link = 'https://weibo.com/{uid}/{bid}'.format(
                            uid=retweet.get('user').get('id'),
                            bid=item.source_id)
                        item.source_author = int(retweet.get('user').get('id'))
                    item.repost_reason = mblog.get('text')
                else:
                    item = WeiboContentItem()
                    item.content = mblog.get('text')
                    if 'pics' in mblog.keys():
                        for pic in mblog.get('pics'):
                            item.pictures.append(pic.get('url'))
                    if 'page_info' in mblog.keys():
                        page_url = mblog.get('page_info').get('page_url')
                        if re.match(r'http://media\.weibo\.cn/article\?.*id=\d+',
                                    page_url):  # 移动端文章链接打不开，将其换为PC端链接
                            article_id = re.search(r'http://media\.weibo\.cn/article\?.*id=(\d+)',
                                                   page_url).group(1)
                            item.media = 'https://weibo.com/ttarticle/p/show?id={id}'.format(
                                id=article_id)
                        else:
                            item.media = page_url
                item.id = mblog.get('bid')
                item.author = int(mblog.get('user').get('id'))
                item.link = 'https://weibo.com/{uid}/{bid}'.format(uid=item.author, bid=item.id)
                item.time = int(time_value)
                item.source = mblog.get('source')
                weibos.append(item)
                if len(weibos) >= number:
                    break
            if stop_flag:
                break
        if self._log:
            logging.info('Succeed in scraping weibos of weibo user: %d.' % id)
        self.scraped_weibos[id] = weibos
        return weibos
