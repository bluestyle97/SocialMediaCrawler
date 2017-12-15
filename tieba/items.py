"""
@author: Jiale Xu
@date: 2017/11/20
@desc: Items for tieba scraping.
"""
from lib.base_item import SocialMediaItem


class TiebaItem(SocialMediaItem):
    pass


class TiebaUserItem(TiebaItem):
    def __init__(self):
        # user's baidu id
        self._name = ''
        # user's sex
        self._sex = ''
        # user's tieba age
        self._tieba_age = 0
        # url user's avatar
        self._avatar = ''
        # number of user's followings
        self._following_count = 0
        # number of user's followers
        self._follower_count = 0
        # number of forums which are followed by user
        self._forum_count = 0
        # number of user's posts
        self._post_count = 0

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
        """User's name."""

        return self._name

    @name.setter
    def name(self, value):
        """Legal user name should be a string."""

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
    def tieba_age(self):
        """User's tieba age, i.e. how long has it been since the user registered tieba account."""

        return self._tieba_age

    @tieba_age.setter
    def tieba_age(self, value):
        """Legal tieba age should be a float number which is positive."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'tieba_age\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'tieba_age\' should be positive.')
        self._tieba_age = value

    @property
    def avatar(self):
        """Link of user's avatar."""

        return self._avatar

    @avatar.setter
    def avatar(self, value):
        """Legal value of avatar should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'avatar\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._avatar = value

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
            raise ValueError('Attribute \'following_count\' should be positive.')
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
            raise ValueError('Attribute \'follower_count\' should be positive.')
        self._follower_count = value

    @property
    def forum_count(self):
        """Number of user's following forums."""

        return self._forum_count

    @forum_count.setter
    def forum_count(self, value):
        """Legal forum count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'forum_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'forum_count\' should be positive.')
        self._forum_count = value

    @property
    def post_count(self):
        """Number of user's posts."""

        return self._post_count

    @post_count.setter
    def post_count(self, value):
        """Legal post count should be a positive integer."""

        if not isinstance(value, int):
            raise TypeError('Attribute \'post_count\' should be an instance of type \'int\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'post_count\' should be positive.')
        self._post_count = value


class TiebaPostItem(TiebaItem):
    def __init__(self):
        # post's created time
        self._time = 0
        # post's title
        self._title = ''
        # post's content
        self._content = ''
        # post's url
        self._link = ''
        # name of the forum which the post belongs to
        self._forum = ''
        # link of the forum which the post belongs to
        self._forum_link = ''

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
        """ Post's created time, a unix timestamp."""

        return self._time

    @time.setter
    def time(self, value):
        """Legal time should be a unix timestamp."""

        if not isinstance(value, float):
            raise TypeError('Attribute \'time\' should be an instance of type \'float\'. '
                            'Found: %s.' % type(value))
        if value < 0:
            raise ValueError('Attribute \'time\' is a unix timestamp, which should be positive.')
        self._time = value

    @property
    def title(self):
        """Title of post."""

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
        """Content of post."""

        return self._content

    @content.setter
    def content(self, value):
        """Legal content should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'content\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._content = value

    @property
    def link(self):
        """Link of post."""

        return self._link

    @link.setter
    def link(self, value):
        """Legal link should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._link = value

    @property
    def forum(self):
        """Name of the forum which the post belongs to."""

        return self._forum

    @forum.setter
    def forum(self, value):
        """Legal forum name should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'forum\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._forum = value

    @property
    def forum_link(self):
        """Link of the forum which the post belongs to."""

        return self._forum_link

    @forum_link.setter
    def forum_link(self, value):
        """Legal forum link should be a string."""

        if not isinstance(value, str):
            raise TypeError('Attribute \'forum_link\' should be an instance of type \'str\'. '
                            'Found: %s.' % type(value))
        self._forum_link = value
