"""
base_item
~~~~~~~~~

This module implements some basic classes for social media scraping.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/05.
:license: MIT License, see LICENSE.txt for more details.
"""
from enum import Enum


class SocialMediaSpider:
    pass


class SocialMediaItem:
    pass


class Sex(Enum):
    FEMALE = 0
    MALE = 1
    UNKNOWN = 2