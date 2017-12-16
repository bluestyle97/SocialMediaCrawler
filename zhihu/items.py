"""
zhihu.item
~~~~~~~~~~

This module implements the items of zhihu scraping.

:copyright: (c) 2017 by Jiale Xu.
:create time: 2017/11/04.
:license: MIT License, see LICENSE.txt for more details.
"""

from lib.base_item import SocialMediaItem


class ZhihuItem(SocialMediaItem):
    pass


class ZhihuUserItem(ZhihuItem):
    def __init__(self):
        # user's id
        self._id = id
        # user's name
        self._name = ''
        # user's sex
        self._sex = ''  # 性别 0为女 1为男 -1为未知
        # link of user's avatar
        self._avatar = ''
        # user's business
        self._business = ''
        # user's headline
        self._headline = ''
        # user's description
        self._description = ''
        # number of user's questions
        self._question_count = 0
        # number of user's answers
        self._answer_count = 0
        # number of user's articles
        self._article_count = 0
        # number of vote-ups obtained by user
        self._voteup_count = 0
        # number of thanks obtained by user
        self._thanked_count = 0
        # number of stars obtained by user
        self._favorited_count = 0
        # number of user's followings
        self._following_count = 0
        # number of user's followers
        self._follower_count = 0
        # number of user's following topics
        self._following_topic_count = 0
        # number of user's following columns
        self._following_column_count = 0
        # number of user's following questions
        self._following_question_count = 0
        # number of user's following favlists
        self._following_favlist_count = 0
        # user's education experiences
        self.educations = []
        # user's employment experiences
        self.employments = []
        # user's living places
        self.locations = []  # 居住地

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Name: ' + str(self._name) + '\n'
        string += 'Sex: ' + str(self._sex) + '\n'
        string += 'Avatar: ' + str(self._avatar) + '\n'
        string += 'Business: ' + str(self._business) + '\n'
        string += 'Headline: ' + str(self._headline) + '\n'
        string += 'Description: ' + str(self._description) + '\n'
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
        """User's id."""

        return self._id

    @id.setter
    def id(self, value):
        """Legal id should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'id\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._id = value

    @property
    def name(self):
        """User's name."""

        return self._name

    @name.setter
    def name(self, value):
        """Legal name should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'name\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._name = value

    @property
    def sex(self):
        """User's sex."""

        return self._sex

    @sex.setter
    def sex(self, value):
        """Legal sex should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'sex\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._sex = value

    @property
    def avatar(self):
        """Link of user's avatar."""

        return self._avatar

    @avatar.setter
    def avatar(self, value):
        """Legal avatar should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'avatar\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._avatar = value

    @property
    def business(self):
        """User's business."""

        return self._business

    @business.setter
    def business(self, value):
        """Legal business should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'business\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._business = value

    @property
    def headline(self):
        """User's headline."""

        return self._headline

    @headline.setter
    def headline(self, value):
        """Legal headline should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'headline\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._headline = value

    @property
    def description(self):
        """User's description."""

        return self._description

    @description.setter
    def description(self, value):
        """Legal description should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'description\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._description = value

    @property
    def question_count(self):
        """Number of user's questions."""

        return self._question_count

    @question_count.setter
    def question_count(self, value):
        """Legal question count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'question_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'question_count\' should be a positive integer.')
        self._question_count = value

    @property
    def answer_count(self):
        """Number of user's answers."""

        return self._answer_count

    @answer_count.setter
    def answer_count(self, value):
        """Legal answer count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'answer_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'answer_count\' should be a positive integer.')
        self._answer_count = value

    @property
    def article_count(self):
        """Number of user's articles."""

        return self._article_count

    @article_count.setter
    def article_count(self, value):
        """Legal article count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'article_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'article_count\' should be a positive integer.')
        self._article_count = value

    @property
    def voteup_count(self):
        """Number of vote-ups obtained by user."""

        return self._voteup_count

    @voteup_count.setter
    def voteup_count(self, value):
        """Legal vote-up count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'voteup_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'voteup_count\' should be a positive integer.')
        self._voteup_count = value

    @property
    def thanked_count(self):
        """Number of thanks obtained by user."""

        return self._thanked_count

    @thanked_count.setter
    def thanked_count(self, value):
        """Legal thanked count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'thanked_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'thanked_count\' should be a positive integer.')
        self._thanked_count = value

    @property
    def favorited_count(self):
        """Number of favorites obtained by user."""

        return self._favorited_count

    @favorited_count.setter
    def favorited_count(self, value):
        """Legal favorites count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'favorited_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'favorited_count\' should be a positive integer.')
        self._favorited_count = value

    @property
    def following_count(self):
        """Number of user's followings."""

        return self._following_count

    @following_count.setter
    def following_count(self, value):
        """Legal following count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'following_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_count\' should be a positive integer.')
        self._following_count = value

    @property
    def follower_count(self):
        """Number of user's followers."""

        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        """Legal follower count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'follower_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'follower_count\' should be a positive integer.')
        self._follower_count = value

    @property
    def following_topic_count(self):
        """Number of user's following topics."""

        return self._following_topic_count

    @following_topic_count.setter
    def following_topic_count(self, value):
        """Legal following topic count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'following_topic_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_topic_count\' should be a positive integer.')
        self._following_topic_count = value

    @property
    def following_column_count(self):
        """Number of user's following columns."""

        return self._following_column_count

    @following_column_count.setter
    def following_column_count(self, value):
        """Legal following column count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'following_column_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_column_count\' should be a positive integer.')
        self._following_column_count = value

    @property
    def following_question_count(self):
        """Number of user's following questions."""

        return self._following_question_count

    @following_question_count.setter
    def following_question_count(self, value):
        """Legal following question count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'following_question_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_question_count\' should be a positive integer.')
        self._following_question_count = value

    @property
    def following_favlist_count(self):
        """Number of user's following favlists."""

        return self._following_favlist_count

    @following_favlist_count.setter
    def following_favlist_count(self, value):
        """Legal following favlist count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'following_favlist_count\' should be an instance of type '
                            '\'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'following_favlist_count\' should be a positive integer.')
        self._following_favlist_count = value


class ZhihuEducationItem(ZhihuItem):
    def __init__(self):
        # school of education
        self._school = ''
        # major of education
        self._major = ''

    def __str__(self):
        string = 'School: ' + str(self._school) + ', Major:' + str(self._major)
        return string

    @property
    def school(self):
        """Return the school of education experience."""

        return self._school

    @school.setter
    def school(self, value):
        """Legal school should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'school\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._school = value

    @property
    def major(self):
        """Return the major of education experience."""

        return self._major

    @major.setter
    def major(self, value):
        """Legal major should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'major\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._major = value


class ZhihuEmploymentItem(ZhihuItem):
    def __init__(self):
        # company of employment
        self._company = ''
        # job of employment
        self._job = ''

    def __str__(self):
        string = 'Company: ' + str(self._company) + ', Job: ' + str(self._job)
        return string

    @property
    def company(self):
        """Return the company of employment experience."""

        return self._company

    @company.setter
    def company(self, value):
        """Legal company should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'company\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._company = value

    @property
    def job(self):
        """Return the job of education experience."""

        return self._job

    @job.setter
    def job(self, value):
        """Legal job should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'job\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._job = value


class ZhihuQuestionItem(ZhihuItem):
    def __init__(self):
        # question's id
        self._id = 0
        # question's title
        self._title = ''
        # question's content
        self._content = ''
        # question's create time
        self._create_time = 0.
        # question's update time
        self._update_time = 0.
        # number of question's followers
        self._follower_count = 0
        # number of question's visit times
        self._visit_count = 0
        # number of question's comments
        self._comment_count = 0
        # list of question's topic tags
        self.topics = []

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Title: ' + str(self._title) + '\n'
        string += 'Content: ' + str(self._content) + '\n'
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
        """Return id of question."""

        return self._id

    @id.setter
    def id(self, value):
        """Legal id should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'id\' should be a positive integer.')
        self._id = value

    @property
    def title(self):
        """Return title of question."""

        return self._title

    @title.setter
    def title(self, value):
        """Legal title should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'title\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._title = value

    @property
    def content(self):
        """Return content of question."""

        return self._content

    @content.setter
    def content(self, value):
        """Legal content should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value

    @property
    def create_time(self):
        """Return create time of question."""

        return self._create_time

    @create_time.setter
    def create_time(self, value):
        """Legal create time should be a positive float number."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'create_time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'create_time\' should be positive.")
        self._create_time = value

    @property
    def update_time(self):
        """Return update time of question."""

        return self._update_time

    @update_time.setter
    def update_time(self, value):
        """Legal update time should be a positive float number."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'update_time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'update_time\' should be positive.")
        self._update_time = value

    @property
    def follower_count(self):
        """Number of question's followers."""

        return self._follower_count

    @follower_count.setter
    def follower_count(self, value):
        """Legal follower count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'follower_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'follower_count\' should be a positive integer.')
        self._follower_count = value

    @property
    def visit_count(self):
        """Number of question's visit times."""

        return self._visit_count

    @visit_count.setter
    def visit_count(self, value):
        """Legal visit count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'visit_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'visit_count\' should be a positive integer.')
        self._visit_count = value

    @property
    def comment_count(self):
        """Number of question's comments."""

        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        """Legal comment count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'comment_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'comment_count\' should be a positive integer.')
        self._comment_count = value


class ZhihuAnswerItem(ZhihuItem):
    def __init__(self):
        # answer's id
        self._id = 0
        # answer's question id
        self._question_id = 0
        # answer's author
        self._author = ''
        # answer's content
        self._content = ''
        # answer's create time
        self._create_time = 0.
        # answer's update time
        self._update_time = 0.
        # number of answer's vote-ups
        self._voteup_count = 0
        # number of answer's comments
        self._comment_count = 0

    def __str__(self):
        string = ''
        string += 'ID: ' + str(self._id) + '\n'
        string += 'Question ID: ' + str(self._question_id) + '\n'
        string += 'Author: ' + str(self._author) + '\n'
        string += 'Content: ' + str(self._content) + '\n'
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
        """Return id of answer."""

        return self._id

    @id.setter
    def id(self, value):
        """Legal id should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'id\' should be a positive integer.')
        self._id = value

    @property
    def question_id(self):
        """Return question id of answer."""

        return self._question_id

    @question_id.setter
    def question_id(self, value):
        """Legal question id should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'question_id\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'question_id\' should be a positive integer.')
        self._question_id = value

    @property
    def author(self):
        """Return author of answer."""

        return self._author

    @author.setter
    def author(self, value):
        """Legal author should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'author\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._author = value

    @property
    def content(self):
        """Return content of answer."""

        return self._content

    @content.setter
    def content(self, value):
        """Legal content should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value

    @property
    def create_time(self):
        """Return create time of answer."""

        return self._create_time

    @create_time.setter
    def create_time(self, value):
        """Legal create time should be a positive float number."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'create_time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'create_time\' should be positive.")
        self._create_time = int(value)

    @property
    def update_time(self):
        """Return update time of answer."""

        return self._update_time

    @update_time.setter
    def update_time(self, value):
        """Legal update time should be a positive float number."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'update_time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'update_time\' should be positive.")
        self._update_time = int(value)

    @property
    def voteup_count(self):
        """Number of answer's vote-ups."""

        return self._voteup_count

    @voteup_count.setter
    def voteup_count(self, value):
        """Legal vote-up count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'voteup_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'voteup_count\' should be a positive integer.')
        self._voteup_count = value

    @property
    def comment_count(self):
        """Number of answer's comments."""

        return self._comment_count

    @comment_count.setter
    def comment_count(self, value):
        """Legal comment count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'comment_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'comment_count\' should be a positive integer.')
        self._comment_count = value


class ZhihuActivityItem(ZhihuItem):
    def __init__(self):
        # activity's create time
        self._time = 0
        # activity's actor
        self._actor = ''
        # activity's action type
        self._action = ''
        # activity's target user
        self._target_user = ''
        # activity's target title
        self._target_title = ''
        # activity's target content
        self._target_content = ''
        # activity's target link
        self._target_link = ''

    def __str__(self):
        string = ''
        string += 'Time: ' + str(self._time) + '\n'
        string += 'Actor: ' + str(self._actor) + '\n'
        string += 'Action: ' + str(self._action) + '\n'
        string += 'Target User: ' + str(self._target_user) + '\n'
        string += 'Target Title: ' + str(self._target_title) + '\n'
        string += 'Target Content: ' + str(self._target_content) + '\n'
        string += 'Target Link: ' + str(self._target_link) + '\n'
        return string

    def __eq__(self, other):
        if not isinstance(other, ZhihuActivityItem):
            return False
        return self._time == other.time and self._actor == other.actor

    @property
    def time(self):
        """Return create time of activity."""

        return self._time

    @time.setter
    def time(self, value):
        """Legal time should be a unix timestamp."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError("Attribute \'time\' should be positive.")
        self._time = value

    @property
    def actor(self):
        """Return actor of activity."""

        return self._actor

    @actor.setter
    def actor(self, value):
        """Legal actor should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'actor\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._actor = value

    @property
    def action(self):
        """Return action of activity."""

        return self._action

    @action.setter
    def action(self, value):
        """Legal action should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'action\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._action = value

    @property
    def target_user(self):
        """Return target user of activity."""

        return self._target_user

    @target_user.setter
    def target_user(self, value):
        """Legal target user should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'target_user\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_user = value

    @property
    def target_title(self):
        """Return target title of activity."""

        return self._target_title

    @target_title.setter
    def target_title(self, value):
        """Legal target title should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'target_title\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_title = value

    @property
    def target_content(self):
        """Return target content of activity."""

        return self._target_content

    @target_content.setter
    def target_content(self, value):
        """Legal target content should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'target_content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_content = value

    @property
    def target_link(self):
        """Return target link of activity."""

        return self._target_link

    @target_link.setter
    def target_link(self, value):
        """Legal target link should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'target_link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._target_link = value
