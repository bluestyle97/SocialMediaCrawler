"""
tieba.items
~~~~~~~~~~~

This module implements the items for tieba scraping.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/20.
:license: MIT License, see LICENSE.txt for more details.
"""
from lib.basis import SocialMediaItem


class TiebaItem(SocialMediaItem):
    pass


class TiebaUserItem(TiebaItem):
    def __init__(self):
        self._name = ''             # 用户名
        self._sex = ''              # 性别
        self._tieba_age = 0         # 吧龄
        self._avatar = ''           # 头像链接
        self._following_count = 0   # 关注数
        self._follower_count = 0    # 粉丝数
        self._forum_count = 0       # 关注的吧数
        self._post_count = 0        # 发帖数

    def __str__(self):
        string = ''
        string += 'Name: ' + str(self._name) + '\n'
        string += 'Sex: ' + str(self._sex) + '\n'
        string += 'Tieba Age: ' + str(self._tieba_age) + '\n'
        string += 'Avatar: ' + str(self._avatar) + '\n'
        string += 'Following Count: ' + str(self._following_count) + '\n'
        string += 'Follower Count: ' + str(self._follower_count) + '\n'
        string += 'Forum Count: ' + str(self._forum_count) + '\n'
        string += 'Post Count: ' + str(self._post_count) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, TiebaUserItem):
            raise TypeError('Compared object should be an instance of type \'TiebaUserItem\'. '
                            'Found: %s.' % type(other))
        return self._name == other.name

    def __hash__(self):
        return hash(self.name)

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
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'sex\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._sex = value

    @property
    def tieba_age(self):
        return self._tieba_age

    @tieba_age.setter
    def tieba_age(self, value):
        if not isinstance(value, float):
            raise TypeError('Attribute \'tieba_age\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'tieba_age\' should be positive.')
        self._tieba_age = value

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

    @property
    def forum_count(self):
        return self._forum_count

    @forum_count.setter
    def forum_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'forum_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'forum_count\' should be positive.')
        self._forum_count = value

    @property
    def post_count(self):
        return self._post_count

    @post_count.setter
    def post_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'post_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'post_count\' should be positive.')
        self._post_count = value


class TiebaPostItem(TiebaItem):
    def __init__(self):
        self._time = 0          # 时间
        self._title = ''        # 标题
        self._content = ''      # 内容
        self._link = ''         # 链接
        self._forum = ''        # 贴吧名
        self._forum_link = ''   # 贴吧链接

    def __str__(self):
        string = ''
        string += 'Time: ' + str(self._time) + '\n'
        string += 'Title: ' + str(self._title) + '\n'
        string += 'Content: ' + str(self._content) + '\n'
        string += 'Link: ' + str(self._link) + '\n'
        string += 'Forum: ' + str(self._forum) + '\n'
        string += 'Forum Link: ' + str(self._forum_link) + '\n'
        return string

    def __hash__(self):
        return hash(self._link)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, float):
            raise TypeError('Attribute \'time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'time\' is a unix timestamp, which should be positive.')
        self._time = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'title\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._title = value

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
    def link(self):
        return self._link

    @link.setter
    def link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._link = value

    @property
    def forum(self):
        return self._forum

    @forum.setter
    def forum(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'forum\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._forum = value

    @property
    def forum_link(self):
        return self._forum_link

    @forum_link.setter
    def forum_link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'forum_link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._forum_link = value
