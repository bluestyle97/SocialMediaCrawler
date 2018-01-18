"""
tieba.spider
~~~~~~~~~~~~

This module implements the spider of baidu tieba.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/20.
:license: MIT License, see LICENSE.txt for more details.
"""
import datetime
import logging
import re
import requests
import os
import time
from urllib.request import quote
from bs4 import BeautifulSoup
from lib.basis import SocialMediaSpider
from lib.configs import tieba_user_homepage_url, tieba_user_post_url
from tieba.items import TiebaUserItem, TiebaPostItem


class TiebaSpider(SocialMediaSpider):
    def __init__(self, log=False, log_dir=''):
        """
        :param log: if True, save logs while scraping; if False, don't save.
        :param log_dir: directory of log files, only available when `log` is True.
        """

        if not isinstance(log, bool):
            raise TypeError('Parameter \'log\' should be an instance of type \'bool\'. '
                            'Found: %s.' % type(log))

        # If `log` is True, then config available path to save log files.
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
            log_file = log_dir + '/tieba-log-%s.log' % (datetime.date.today())
            logging.basicConfig(
                filename=log_file,
                format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                level=10)
        # If `log` is False, do nothing.
        else:
            self._log = False

    def scrape_user_info(self, user):
        """
        Scrape the information of a user.
        :param user: name of the user who is to be scraped
        :return: `TiebaUserItem` object
        """

        assert isinstance(user, str), 'Parameter \'user\' isn\'t an instance of type \'str\'!'

        # Start scraping.
        if self._log:
            logging.info('Scraping info of tieba user: %s...' % user)

        response = requests.get(tieba_user_homepage_url.format(user=quote(user)))
        bs = BeautifulSoup(response.text, 'lxml')

        item = TiebaUserItem()
        item.name = user
        if bs.find('span', {'class': 'userinfo_sex_male'}) is not None:
            item.sex = '男'
        else:
            item.sex = '女'
        age = bs.find('span', {'class': 'user_name'}).find_all('span')[2].get_text()
        item.tieba_age = float(re.search(r'吧龄:(.*)年', age).group(1))
        item.avatar = bs.find('a', {'class': 'userinfo_head'}).img.attrs['src']
        item.following_count = int(
            bs.find_all('span', {'class': 'concern_num'})[0].find('a').get_text())
        item.follower_count = int(bs.find_all('span', {'class': 'concern_num'})[1].find(
            'a').get_text())
        # The first few forums lies in this div.
        forum_div1 = bs.find('div', {'id': 'forum_group_wrap'})
        # Others forums can't be seen until we spread them out on the web page.
        forum_div2 = bs.find('div', {'class': 'j_panel_content'})
        if forum_div1 is not None:
            forum_items1 = forum_div1.find_all('a', {'class': 'unsign'})
            item.forum_count += len(forum_items1)
        if forum_div2 is not None:
            forum_items2 = forum_div2.find_all('a', {'class': 'unsign'})
            item.forum_count += len(forum_items2)
        post = bs.find('span', {'class': 'user_name'}).find_all('span')[4].get_text()
        item.post_count = int(re.search(r'发贴:(\d+)', post).group(1))

        # Scraping finished.
        if self._log:
            logging.info('Succeed in scraping info of tieba user: %s.' % user)

        return item

    def scrape_user_forum(self, user):
        """
        Scrape the names of forums which are followed by the user.
        :param user: name of the user who is to be scraped
        :return: list of forum names
        """

        assert isinstance(user, str), 'Parameter \'user\' isn\'t an instance of type \'str\'!'

        # Start scraping.
        if self._log:
            logging.info('Scraping forums of tieba user: %s...' % user)

        response = requests.get(tieba_user_homepage_url.format(user=quote(user)))
        bs = BeautifulSoup(response.text, 'lxml')

        # The first few forums lies in this div.
        forum_div1 = bs.find('div', {'id': 'forum_group_wrap'})
        # Others forums can't be seen until we spread them out on the web page.
        forum_div2 = bs.find('div', {'class': 'j_panel_content'})
        forums = []
        if forum_div1 is not None:
            for forum_a in forum_div1.find_all('a', {'class': 'unsign'}):
                forums.append(forum_a.span.get_text())
        if forum_div2 is not None:
            for forum_a in forum_div2.find_all('a', {'class': 'unsign'}):
                forums.append(forum_a.get_text())

        # Scraping finished.
        if self._log:
            logging.info('Succeed in scraping forums of tieba user: %s.' % user)

        return forums

    def scrape_user_post(self, user, before=None, after=None, number=1):
        """
        Scrape the posts of the user.
        :param user: name of the user who is to be scraped
        :param before: a timestamp, representing the latest time we care about
        :param after: a timestamp, representing the earliest time we care about
        :param number: number of posts we want to get
        :return: list of `TiebaPostItem` objects
        """

        assert isinstance(user, str), 'Parameter \'user\' isn\'t an instance of type \'str\'!'
        assert isinstance(number, int), 'Parameter \'number\' isn\'t an instance of type \'int\'!'
        assert number >= 1, 'Parameter \'number\' is smaller than 1!'

        # By default, we care about any available time, from 0 to current time.
        before = int(time.time()) if before is None else int(before)
        after = 0 if after is None else int(after)

        # Start scraping.
        if self._log:
            logging.info('Scraping posts of tieba user: %s...' % user)

        posts = []
        page = 1
        stop_flag = False
        while len(posts) < number:
            # Sometimes we get 404 page, so we user a loop to retry.
            while True:
                response = requests.get(tieba_user_post_url.format(user=user, page=page))
                if response.text.startswith('<!DOCTYPE html>'):
                    time.sleep(3)
                else:
                    break
            result = response.json()
            for thread in result.get('data').get('thread_list'):
                if len(posts) >= number:
                    break
                item = TiebaPostItem()
                item.time = float(thread.get('create_time'))
                if item.time > before:
                    continue
                if item.time < after:
                    stop_flag = True
                    break
                item.title = thread.get('title')
                if re.match(r'^回复：', item.title):
                    item.title = item.title[3:]
                item.content = thread.get('content')
                item.link = 'http://tieba.baidu.com/p/{tid}?pid={pid}&cid=#{cid}'.format(
                    tid=thread.get('thread_id'), pid=thread.get('post_id'),
                    cid=thread.get('post_id'))
                item.forum = thread.get('forum_name')
                item.forum_link = 'http://tieba.baidu.com/f?kw={kw}'.format(kw=quote(item.forum))
                posts.append(item)
            page += 1
            if not result.get('data').get('has_more') or stop_flag:
                break

        # Scraping finished.
        if self._log:
            logging.info('Succeed in scraping posts of tieba user: %s.' % user)

        return posts
