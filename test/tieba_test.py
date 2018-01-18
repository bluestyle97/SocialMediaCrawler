"""
test.qzone_test
~~~~~~~~~~~~~~~

This module is prepared for testing tieba spider.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/25.
:license: MIT License, see LICENSE.txt for more details.
"""
from tieba.spider import TiebaSpider


spider = TiebaSpider()


def scrape_user_info_test(user):
    info = spider.scrape_user_info(user)
    print(info)


def scrape_user_forums_test(user):
    forums = spider.scrape_user_forum(user)
    for forum in forums:
        print(forum)


def scrape_user_posts_test(user, before=None, after=None, number=10):
    posts = spider.scrape_user_post(user, before, after, number)
    for post in posts:
        print(post)


scrape_user_info_test('愛你沒法說')
scrape_user_forums_test('愛你沒法說')
scrape_user_posts_test('颜落_mmmmz', number=30)
