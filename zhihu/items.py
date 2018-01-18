"""
zhihu.items
~~~~~~~~~~~

This module implements the items for zhihu scraping.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/04.
:license: MIT License, see LICENSE.txt for more details.
"""

from lib.basis import SocialMediaItem, Sex


class ZhihuItem(SocialMediaItem):
    pass


class ZhihuUserItem(ZhihuItem):
    def __init__(self):
        self._id = ''                       # 用户ID
        self._name = ''                     # 用户名
        self._sex = Sex.UNKNOWN             # 性别
        self._avatar = ''                   # 头像链接
        self._business = ''                 # 行业
        self._headline = ''                 # 一句话描述
        self._description = ''              # 个人介绍
        self._question_count = 0            # 提问数
        self._answer_count = 0              # 回答数
        self._article_count = 0             # 文章数
        self._voteup_count = 0              # 得到的赞同数
        self._thanked_count = 0             # 得到的感谢数
        self._favorited_count = 0           # 得到的收藏数
        self._following_count = 0           # 关注数
        self._follower_count = 0            # 粉丝数
        self._following_topic_count = 0     # 关注的话题数
        self._following_column_count = 0    # 关注的专栏数
        self._following_question_count = 0  # 关注的问题数
        self._following_favlist_count = 0   # 关注的收藏夹数
        self.educations = []                # 教育经历
        self.employments = []               # 职业经历
        self.locations = []                 # 居住地

    def __str__(self):
        string = ''
        string += 'ID: ' + self._id + '\n'
        string += 'Name: ' + self._name + '\n'
        string += 'Sex: ' + self._sex.name + '\n'
        string += 'Avatar: ' + self._avatar + '\n'
        string += 'Business: ' + self._business + '\n'
        string += 'Headline: ' + self._headline + '\n'
        string += 'Description: ' + self._description + '\n'
        string += 'Question Count: ' + str(self._question_count) + '\n'
        string += 'Answer Count: ' + str(self._answer_count) + '\n'
        string += 'Article Count: ' + str(self._article_count) + '\n'
        string += 'Vote-up Count: ' + str(self._voteup_count) + '\n'
        string += 'Thanked Count: ' + str(self._thanked_count) + '\n'
        string += 'Favorited Count: ' + str(self._favorited_count) + '\n'
        string += 'Following Count: ' + str(self._following_count) + '\n'
        string += 'Follower Count: ' + str(self._follower_count) + '\n'
        string += 'Following Topic Count: ' + str(self._following_topic_count) + '\n'
        string += 'Following Column Count: ' + str(self._following_column_count) + '\n'
        string += 'Following Question Count: ' + str(self._following_question_count) + '\n'
        string += 'Following Favlist Count: ' + str(self._following_favlist_count) + '\n'
        string += 'Educations: ' + '; '.join([str(edu) for edu in self.educations]) + '\n'
        string += 'Employments: ' + '; '.join([str(emp) for emp in self.employments]) + '\n'
        string += 'Locations: ' + '; '.join([str(loc) for loc in self.locations]) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, ZhihuUserItem):
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
        if not isinstance(value, Sex):
            raise TypeError('Attribute \'sex\' should be an instance of type \'Sex\'. '
                            'Found: %s.' % type(value))
        self._sex = value

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
    def business(self):
        return self._business

    @business.setter
    def business(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'business\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._business = value

    @property
    def headline(self):
        return self._headline

    @headline.setter
    def headline(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'headline\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._headline = value

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
    def question_count(self):
        return self._question_count

    @question_count.setter
    def question_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'question_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'question_count\' should be a positive integer.')
        self._question_count = value

    @property
    def answer_count(self):
        return self._answer_count

    @answer_count.setter
    def answer_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'answer_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'answer_count\' should be a positive integer.')
        self._answer_count = value

    @property
    def article_count(self):
        return self._article_count

    @article_count.setter
    def article_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'article_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'article_count\' should be a positive integer.')
        self._article_count = value

    @property
    def voteup_count(self):
        return self._voteup_count

    @voteup_count.setter
    def voteup_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'voteup_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'voteup_count\' should be a positive integer.')
        self._voteup_count = value

    @property
    def thanked_count(self):
        return self._thanked_count

    @thanked_count.setter
    def thanked_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'thanked_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'thanked_count\' should be a positive integer.')
        self._thanked_count = value

    @property
    def favorited_count(self):
        return self._favorited_count

    @favorited_count.setter
    def favorited_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'favorited_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'favorited_count\' should be a positive integer.')
        self._favorited_count = value

    @property
    def following_count(self):
        return self._following_count

    @following_count.setter
    def following_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_count\' should be a positive integer.')
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
            raise ValueError('Attribute \'follower_count\' should be a positive integer.')
        self._follower_count = value

    @property
    def following_topic_count(self):
        return self._following_topic_count

    @following_topic_count.setter
    def following_topic_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_topic_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_topic_count\' should be a positive integer.')
        self._following_topic_count = value

    @property
    def following_column_count(self):
        return self._following_column_count

    @following_column_count.setter
    def following_column_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_column_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_column_count\' should be a positive integer.')
        self._following_column_count = value

    @property
    def following_question_count(self):
        return self._following_question_count

    @following_question_count.setter
    def following_question_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_question_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_question_count\' should be a positive integer.')
        self._following_question_count = value

    @property
    def following_favlist_count(self):
        return self._following_favlist_count

    @following_favlist_count.setter
    def following_favlist_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'following_favlist_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_favlist_count\' should be a positive integer.')
        self._following_favlist_count = value


class ZhihuEducationItem(ZhihuItem):
    def __init__(self):
        self._school = ''   # 学校
        self._major = ''    # 专业

    def __str__(self):
        string = 'School: ' + self._school + ', Major:' + self._major
        return string

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'school\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._school = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'major\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._major = value


class ZhihuEmploymentItem(ZhihuItem):
    def __init__(self):
        self._company = ''  # 公司
        self._job = ''      # 职位

    def __str__(self):
        string = 'Company: ' + self._company + ', Job: ' + self._job
        return string

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'company\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._company = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'job\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._job = value


class ZhihuQuestionItem(ZhihuItem):
    def __init__(self):
        self._id = 0                # 问题ID
        self._title = ''            # 标题
        self._content = ''          # 内容
        self._create_time = 0       # 创建时间
        self._update_time = 0       # 更新时间
        self._follower_count = 0    # 关注数
        self._visit_count = 0       # 浏览数
        self._comment_count = 0     # 评论数
        self.topics = []            # 话题标签列表

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Title: ' + self._title + '\n'
        string += 'Content: ' + self._content + '\n'
        string += 'Create Time: ' + str(self._create_time) + '\n'
        string += 'Update Time: ' + str(self._update_time) + '\n'
        string += 'Follower Count: ' + str(self._follower_count) + '\n'
        string += 'Visit Count: ' + str(self._visit_count) + '\n'
        string += 'Comment Count: ' + str(self._comment_count) + '\n'
        string += 'Topics: ' + '; '.join([str(top) for top in self.topics]) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, ZhihuQuestionItem):
            return False
        return self._id == other.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'id\' should be a positive integer.')
        self._id = value

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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'create_time\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'create_time\' should be positive.")
        self._create_time = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'update_time\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'update_time\' should be positive.")
        self._update_time = value

    @property
    def follower_count(self):
        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'follower_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'follower_count\' should be a positive integer.')
        self._follower_count = value

    @property
    def visit_count(self):
        return self._visit_count

    @visit_count.setter
    def visit_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'visit_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'visit_count\' should be a positive integer.')
        self._visit_count = value

    @property
    def comment_count(self):
        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'comment_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'comment_count\' should be a positive integer.')
        self._comment_count = value


class ZhihuAnswerItem(ZhihuItem):
    def __init__(self):
        self._id = 0                # 答案ID
        self._question_id = 0       # 问题ID
        self._author = ''           # 答主
        self._content = ''          # 内容
        self._create_time = 0       # 创建时间
        self._update_time = 0       # 更新时间
        self._voteup_count = 0      # 赞同数
        self._comment_count = 0     # 评论数

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Question ID: ' + str(self._question_id) + '\n'
        string += 'Author: ' + self._author + '\n'
        string += 'Content: ' + self._content + '\n'
        string += 'Create Time: ' + str(self._create_time) + '\n'
        string += 'Update Time: ' + str(self._update_time) + '\n'
        string += 'Vote-up Count: ' + str(self._voteup_count) + '\n'
        string += 'Comment Count: ' + str(self._comment_count) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, ZhihuAnswerItem):
            return False
        return self._id == other.id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'id\' should be a positive integer.')
        self._id = value

    @property
    def question_id(self):
        return self._question_id

    @question_id.setter
    def question_id(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'question_id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'question_id\' should be a positive integer.')
        self._question_id = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'author\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._author = value

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
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'create_time\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'create_time\' should be positive.")
        self._create_time = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'update_time\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'update_time\' should be positive.")
        self._update_time = value

    @property
    def voteup_count(self):
        return self._voteup_count

    @voteup_count.setter
    def voteup_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'voteup_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'voteup_count\' should be a positive integer.')
        self._voteup_count = value

    @property
    def comment_count(self):
        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        if not isinstance(value, int):
            raise TypeError('Attribute \'comment_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'comment_count\' should be a positive integer.')
        self._comment_count = value


class ZhihuActivityItem(ZhihuItem):
    def __init__(self):
        self._time = 0              # 时间
        self._actor = ''            # 主人
        self._action = ''           # 动态类型
        self._target_user = ''      # 目标用户名
        self._target_title = ''     # 目标标题
        self._target_content = ''   # 目标内容
        self._target_link = ''      # 目标链接

    def __str__(self):
        string = ''
        string += 'Time: ' + str(self._time) + '\n'
        string += 'Actor: ' + self._actor + '\n'
        string += 'Action: ' + self._action + '\n'
        string += 'Target User: ' + self._target_user + '\n'
        string += 'Target Title: ' + self._target_title + '\n'
        string += 'Target Content: ' + self._target_content + '\n'
        string += 'Target Link: ' + self._target_link + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, ZhihuActivityItem):
            return False
        return self._time == other.time and self._actor == other.actor

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
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'actor\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._actor = value

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'action\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._action = value

    @property
    def target_user(self):
        return self._target_user

    @target_user.setter
    def target_user(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'target_user\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_user = value

    @property
    def target_title(self):
        return self._target_title

    @target_title.setter
    def target_title(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'target_title\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_title = value

    @property
    def target_content(self):
        return self._target_content

    @target_content.setter
    def target_content(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'target_content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_content = value

    @property
    def target_link(self):
        return self._target_link

    @target_link.setter
    def target_link(self, value):
        if not isinstance(value, str):
            raise TypeError('Attribute \'target_link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_link = value
