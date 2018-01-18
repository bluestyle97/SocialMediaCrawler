"""
weibo.items
~~~~~~~~~~~

This module implements the items for weibo scraping.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/10/23.
:license: MIT License, see LICENSE.txt for more details.
"""
from lib.basis import SocialMediaItem, Sex


class WeiboItem(SocialMediaItem):
    pass


class WeiboUserItem(WeiboItem):
    def __init__(self):
        self._id = 0
        self._name = ''
        self._avatar = ''
        self._link = ''
        self._sex = Sex.UNKNOWN
        self._location = ''
        self._description = ''
        self._signup_time = ''
        self._weibo_count = 0
        self._following_count = 0
        self._follower_count = 0

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Name: ' + self._name + '\n'
        string += 'Avatar: ' + self._avatar + '\n'
        string += 'Link: ' + self._link + '\n'
        string += 'Sex: ' + self._sex.name + '\n'
        string += 'Location: ' + self._location + '\n'
        string += 'Description: ' + self._description + '\n'
        string += 'Sign-up Time: ' + self._signup_time + '\n'
        string += 'Weibo Count: ' + str(self._weibo_count) + '\n'
        string += 'Following Count: ' + str(self._following_count) + '\n'
        string += 'Follower Count: ' + str(self._follower_count) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, WeiboUserItem):
            return False
        return self.id == other.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'id\' should be positive.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'name\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._name = value

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'avatar\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._avatar = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._link = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if not isinstance(value, Sex):
            raise TypeError('Attribute \'sex\' should be an instance of type \'Sex\'. '
                            'Found: %s.' % type(value))
        self._sex = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'location\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._location = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'description\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._description = value

    @property
    def signup_time(self):
        return self._signup_time

    @signup_time.setter
    def signup_time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'signup_time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._signup_time = value

    @property
    def weibo_count(self):
        return self._weibo_count

    @weibo_count.setter
    def weibo_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'weibo_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'weibo_count\' should be positive.')
        self._weibo_count = value

    @property
    def following_count(self):
        return self._following_count

    @following_count.setter
    def following_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_count\' should be positive.')
        self._following_count = value

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'follower_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'follower_count\' should be positive.')
        self._follower_count = value


class WeiboContentItem(WeiboItem):
    def __init__(self):
        self._author = 0    # 博主ID
        self._time = 0      # 时间
        self._id = ''       # 微博ID
        self._link = ''     # 微博链接
        self._content = ''  # 内容
        self._source = ''   # 来源
        self._media = ''    # 媒体内容链接
        self.pictures = []  # 图片列表

    def __str__(self):
        string = ''
        string += 'Author: ' + str(self._author) + '\n'
        string += 'Time: ' + str(self._time) + '\n'
        string += 'ID: ' + self._id + '\n'
        string += 'Link: ' + self._link + '\n'
        string += 'Content: ' + self._content + '\n'
        string += 'Source: ' + self._source + '\n'
        string += 'Media: ' + self._media + '\n'
        string += 'Pictures: ' + '; '.join(str(pic) for pic in self.pictures) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, WeiboContentItem):
            return False
        return self._id == other.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'id\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._id = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'author\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'author\' should be positive.")
        self._author = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'time\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'time\' should be positive.")
        self._time = value

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._link = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'source\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._source = value

    @property
    def media(self):
        return self._media

    @media.setter
    def media(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'media\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._media = value


class WeiboRepostContentItem(WeiboContentItem):
    def __init__(self):
        WeiboContentItem.__init__(self)
        self._source_author = 0     # 原博主ID
        self._source_id = ''        # 原博ID
        self._source_link = ''      # 原博链接
        self._repost_reason = ''    # 转发理由

    def __str__(self):
        string = WeiboContentItem.__str__(self)
        string += 'Source Author: ' + str(self._source_author) + '\n'
        string += 'Source ID: ' + self._source_id + '\n'
        string += 'Source Link: ' + self._source_link + '\n'
        string += 'Repost Reason: ' + self._repost_reason + '\n'
        return string

    def __hash__(self):
        return hash(self.id)

    @property
    def source_author(self):
        return self._source_author

    @source_author.setter
    def source_author(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'source_author\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'source_author\' should be positive.')
        self._source_author = value

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'source_id\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._source_id = value

    @property
    def source_link(self):
        return self._source_link

    @source_link.setter
    def source_link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'source_link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._source_link = value

    @property
    def repost_reason(self):
        return self._repost_reason

    @repost_reason.setter
    def repost_reason(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'repost_reason\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._repost_reason = value
