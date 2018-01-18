"""
qzone.items
~~~~~~~~~~~

This module implements the items for qzone scraping.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/10/27.
:license: MIT License, see LICENSE.txt for more details.
"""
from lib.basis import SocialMediaItem


class QzoneItem(SocialMediaItem):
    pass


class QzoneUserItem(QzoneItem):
    def __init__(self):
        self._qq = 0         # QQ号
        self._name = ''      # 昵称

    def __str__(self):
        return 'QQ: ' + str(self.qq) + '; Name: ' + str(self.name)

    def __hash__(self):
        return hash(self.qq)

    @property
    def qq(self):
        return self._qq

    @qq.setter
    def qq(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'qq\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'qq\' should be positive.")
        self._time = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'name\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._name = value


class QzoneEmotionItem(QzoneItem):
    def __init__(self):
        self._id = ''                   # 说说ID
        self._owner = QzoneUserItem()   # 主人
        self._time = ''                 # 时间
        self._content = ''              # 内容
        self.pictures = []              # 图片列表
        self._source = ''               # 设备名称
        self._location = ''             # 位置
        self.visitors = []              # 浏览者列表
        self.likers = []                # 点赞者列表
        self.comments = []              # 评论列表

    def __str__(self):
        string = ''
        string += 'ID: ' + self._id + '\n'
        string += 'Owner: ' + str(self._owner) + '\n'
        string += 'Time: ' + self._time + '\n'
        string += 'Content: ' + str(self._content) + '\n'
        string += 'Pictures: ' + '; '.join([str(pic) for pic in self.pictures]) + '\n'
        string += 'Source: ' + str(self._source) + '\n'
        string += 'Location: ' + str(self._location) + '\n'
        string += 'Visitor Count: ' + str(len(self.visitors)) + '\n'
        string += 'Liker Count: ' + str(len(self.likers)) + '\n'
        string += 'Comment Count: ' + str(len(self.comments)) + '\n'
        return string

    def __hash__(self):
        return hash(self.id)

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
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, QzoneUserItem):
            raise TypeError('Attribute \'owner\' should be an instance of type \'QzoneUserItem\'. '
                            'Found: %s.' % type(value))
        self._owner = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._time = value

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
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'location\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._location = value


class QzoneRepostEmotionItem(QzoneEmotionItem):
    def __init__(self):
        QzoneEmotionItem.__init__(self)
        self._repost_source = QzoneUserItem()    # 转发来源
        self._repost_reason = ''                 # 转发理由

    def __str__(self):
        string = QzoneEmotionItem.__str__(self)
        string += 'Repost Source: ' + str(self._repost_source) + '\n'
        string += 'Repost Reason: ' + self._repost_reason + '\n'
        return string

    def __hash__(self):
        return hash(self.id)

    @property
    def repost_source(self):
        return self._repost_source

    @repost_source.setter
    def repost_source(self, value):
        if not isinstance(value, QzoneUserItem):
            raise TypeError('Attribute \'repost_source\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._repost_source = value

    @property
    def repost_reason(self):
        return self._repost_reason

    @repost_reason.setter
    def repost_reason(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'repost_reason\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._repost_reason = value


class QzoneCommentItem(QzoneItem):
    def __init__(self):
        self._commenter = QzoneUserItem()   # 评论者
        self._time = ''                     # 评论时间
        self._content = ''                  # 评论内容
        self.pictures = []                  # 评论图片列表
        self.replies = []                   # 评论回复列表

    def __str__(self):
        string = ''
        string += 'Commenter: ' + str(self._commenter) + '\n'
        string += 'Time: ' + self._time + '\n'
        string += 'Content: ' + str(self._content) + '\n'
        string += 'Pictures: ' + '; '.join([str(pic) for pic in self.pictures]) + '\n'
        string += 'Reply Number: ' + str(len(self.replies)) + '\n'
        return string

    def __hash__(self):
        return hash(self._content)

    @property
    def commenter(self):
        return self._commenter

    @commenter.setter
    def commenter(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'commenter\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._commenter = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._time = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value


class QzoneCommentReplyItem(QzoneItem):
    def __init__(self):
        self._replier = QzoneUserItem()      # 回复者
        self._replyto = QzoneUserItem()      # 回复对象
        self._time = ''                      # 回复时间
        self._content = ''                   # 回复内容

    def __str__(self):
        return self._time + ' ' + self._replier.name + ' reply to ' + self._replyto.name + ': ' + self._content

    def __hash__(self):
        return hash(self._content)

    @property
    def replier(self):
        return self._replier

    @replier.setter
    def replier(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'replier\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._replier = value

    @property
    def replyto(self):
        return self._replyto

    @replyto.setter
    def replyto(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'replyto\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._replyto = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._time = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value


class QzoneMessageItem(QzoneItem):
    def __init__(self):
        self._id = ''                       # 留言ID
        self._owner = QzoneUserItem()       # 主人
        self._poster = QzoneUserItem()      # 留言者
        self._time = ''                     # 留言时间
        self._content = ''                  # 留言内容
        self.replies = []                   # 留言回复列表

    def __str__(self):
        string = ''
        string += 'Owner: ' + str(self._owner) + '\n'
        string += 'Poster: ' + str(self._poster) + '\n'
        string += 'Time: ' + self._time + '\n'
        string += 'Content: ' + self._content + '\n'
        string += 'Replies: ' + '; '.join([str(reply) for reply in self.replies]) + '\n'
        return string

    def __hash__(self):
        return hash(self._id)

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
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, QzoneUserItem):
            raise TypeError('Attribute \'owner\' should be an instance of type \'QzoneUserItem\'. '
                            'Found: %s.' % type(value))
        self._owner = value

    @property
    def poster(self):
        return self._poster

    @poster.setter
    def poster(self, value):
        if not isinstance(value, QzoneUserItem):
            raise TypeError('Attribute \'poster\' should be an instance of type \'QzoneUserItem\'. '
                            'Found: %s.' % type(value))
        self._poster = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._time = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value


class QzoneMessageReplyItem(QzoneItem):
    def __init__(self):
        self._replier = QzoneUserItem()      # 回复者
        self._time = ''                      # 回复时间
        self._content = ''                   # 回复内容

    def __str__(self):
        return self._time + ' ' + self._replier.name + ' replied: ' + self._content

    def __hash__(self):
        return hash(self.content)

    @property
    def replier(self):
        return self._replier

    @replier.setter
    def replier(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'replier\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._replier = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'time\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._time = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value
