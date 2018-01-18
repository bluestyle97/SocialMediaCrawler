"""
test.qzone_test
~~~~~~~~~~~~~~~

This module is prepared for testing qzone spider.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/25.
:license: MIT License, see LICENSE.txt for more details.
"""
from qzone.spider import QzoneSpider


spider = QzoneSpider(0, 'password')
spider.login()


def scrape_emotion_test(qq, number):
    emotions = spider.scrape_emotion(qq, number)
    for emotion in emotions:
        print(emotion)


def scrape_message_test(qq, number):
    messages = spider.scrape_emotion(qq, number)
    for message in messages:
        print(message)


scrape_emotion_test(690147660, 10)
scrape_message_test(690147660, 10)
