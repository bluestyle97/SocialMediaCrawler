"""
zhihu.spider
~~~~~~~~~~~~

This module implements the spider of zhihu.

:copyright: (c) 2017 by Jiale Xu.
:date: 2017/11/01.
:license: MIT License, see LICENSE.txt for more details.
"""
import csv
import datetime
import logging
import os
import re
import requests
import time
from bs4 import BeautifulSoup
from lib.basis import SocialMediaSpider, Sex
from lib.configs import zhihu_user_activity_url, zhihu_answer_query, zhihu_answer_url, \
    zhihu_follower_query, zhihu_user_follower_url, zhihu_following_query, zhihu_user_following_url, \
    zhihu_header, zhihu_question_answer_url, zhihu_question_query, zhihu_question_url, \
    zhihu_user_answer_url, zhihu_user_query, zhihu_user_question_url, zhihu_user_info_url
from zhihu.items import *


class ZhihuSpider(SocialMediaSpider):
    def __init__(self, log=False, log_dir=''):
        """
        :param log: if True, save logs while scraping; if False, don't save.
        :param log_dir: directory of log files, only available when `log` is True.
        """
        assert isinstance(log, bool), 'Parameter \'log\' should be an instance of type \'bool\'. ' \
                                      'Found: %s.' % type(log)

        # If `log` is True, then configure available path in order to save log files.
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
            log_file = log_dir + '/zhihu-log-%s.log' % (datetime.date.today())
            logging.basicConfig(
                filename=log_file,
                format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                level=10)
        # If `log` is False, do nothing.
        else:
            self._log = False

        self._user_info = {}
        self._user_following = {}
        self._user_follower = {}
        self._question = {}
        self._user_question = {}
        self._answer = {}
        self._question_answer = {}
        self._user_answer = {}

    def scrape_user_info(self, user):
        assert isinstance(user, str), 'Parameter \'user\' should be an instance of type \'str\'!'

        if self._log:
            logging.info('Scraping info of zhihu user: %s...' % user)

        response = requests.get(zhihu_user_info_url.format(user=user, include=zhihu_user_query),
                                headers=zhihu_header)
        if response.status_code == 404:  # the user doesn't exist or has been blocked
            if self._log:
                logging.warning('404 error. The user doesn\'t exist or has been blocked.')
            return None
        result = response.json()
        if result.get('error') is not None:  # your identity hasn't been certificated
            if self._log:
                logging.warning('Your identity hasn\'t been confirmed.')
            return None

        item = ZhihuUserItem()
        item.id = result.get('id')
        item.name = result.get('name')
        sex = result.get('gender')
        if sex == 0:
            item.sex = Sex.FEMALE
        elif sex == 1:
            item.sex = Sex.MALE
        item.avatar = result.get('avatar_url')
        if 'business' in result.keys():
            item.business = result.get('business').get('name')
        item.headline = result.get('headline')
        item.description = result.get('description')
        item.question_count = result.get('question_count')
        item.answer_count = result.get('answer_count')
        item.article_count = result.get('articles_count')
        item.voteup_count = result.get('voteup_count')
        item.thanked_count = result.get('thanked_count')
        item.favorited_count = result.get('favorited_count')
        item.following_count = result.get('following_count')
        item.follower_count = result.get('follower_count')
        item.following_topic_count = result.get('following_topic_count')
        item.following_column_count = result.get('following_columns_count')
        item.following_question_count = result.get('following_question_count')
        item.following_favlist_count = result.get('following_favlists_count')
        educations = result.get('educations')
        if educations is not None:
            for education in educations:
                edu_item = ZhihuEducationItem()
                edu_item.school = education.get('school').get('name')
                if 'major' in education.keys():
                    edu_item.major = education.get('major').get('name')
                item.educations.append(edu_item)
        employments = result.get('employments')
        if employments is not None:
            for employment in employments:
                emp_item = ZhihuEmploymentItem()
                if 'company' in employment.keys():
                    emp_item.company = employment.get('company').get('name')
                if 'job' in employment.keys():
                    emp_item.job = employment.get('job').get('name')
                item.employments.append(emp_item)
        locations = result.get('locations')
        if locations is not None:
            for location in locations:
                item.locations.append(location.get('name'))

        if self._log:
            logging.info('Succeed in scraping info of zhihu user: %s.' % user)

        self._user_info[user] = item
        return item

    def scrape_user_following(self, user, number=1):
        assert isinstance(user, str), 'Parameter \'user\' should be an instance of type \'str\'!'
        assert isinstance(number, int) and number >= 1, 'Parameter \'number\' should be an integer which is bigger than 1!'

        if self._log:
            logging.info('Scraping follows of zhihu user: %s...' % user)

        response = requests.get(
            zhihu_user_following_url.format(
                user=user, include=zhihu_following_query, offset=0, limit=20),
            headers=zhihu_header)
        if response.status_code == 404:  # the user doesn't exist or has been blocked
            if self._log:
                logging.warning('404 error. The user doesn\'t exist or has been blocked.')
            return []
        result = response.json()
        total = result.get('paging').get('totals')
        number = min((number, total))
        url_tokens = []
        while len(url_tokens) < number:
            for data in result.get('data'):
                url_tokens.append(data.get('url_token'))
                if len(url_tokens) >= number:
                    break
            if len(url_tokens) >= number:
                break
            next_page = result.get('paging').get('next')
            result = requests.get(next_page, headers=zhihu_header).json()
        followings = []
        for url_token in url_tokens:
            item = self.scrape_user_info(user=url_token)
            followings.append(item)

        if self._log:
            logging.info('Succeed in scraping follows of zhihu user: %s.' % user)

        self._user_following[user] = followings
        return followings

    def scrape_user_follower(self, user, number=1):
        assert isinstance(user, str), 'Parameter \'user\' should be an instance of type \'str\'!'
        assert isinstance(number, int) and number >= 1, 'Parameter \'number\' should be an integer which is bigger than 1!'

        if self._log:
            logging.info('Scraping followers of zhihu user: %s...' % user)

        response = requests.get(
            zhihu_user_follower_url.format(user=user, include=zhihu_follower_query, offset=0,
                                           limit=20), headers=zhihu_header)
        if response.status_code == 404:  # the user doesn't exist or has been blocked
            if self._log:
                logging.warning('404 error. The user doesn\'t exist or has been blocked.')
            return []
        result = response.json()
        total = result.get('paging').get('totals')
        number = min((number, total))
        url_tokens = []
        while len(url_tokens) < number:
            for data in result.get('data'):
                url_tokens.append(data.get('url_token'))
                if len(url_tokens) >= number:
                    break
            if len(url_tokens) >= number:
                break
            next_page = result.get('paging').get('next')
            result = requests.get(next_page, headers=zhihu_header).json()
        followers = []
        for url_token in url_tokens:
            item = self.scrape_user_info(user=url_token)
            followers.append(item)

        if self._log:
            logging.info('Succeed in scraping followers of zhihu user: %s.' % user)

        self._user_follower[user] = followers
        return followers

    def scrape_user_activity(self, user, before=None, after=None, number=1):
        assert isinstance(user, str), 'Parameter \'user\' should be an instance of type \'str\'!'
        assert isinstance(number, int) and number >= 1, 'Parameter \'number\' should be an integer which is bigger than 1!'

        before = int(time.time()) if before is None else int(before)
        after = 0 if after is None else int(after)

        if self._log:
            logging.info('Scraping activities of zhihu user: %s...' % user)

        response = requests.get(zhihu_user_activity_url.format(user=user, limit=10, after=before),
                                headers=zhihu_header)
        result = response.json()
        activities = []
        stop_flag = False
        while len(activities) < number:
            for data in result.get('data'):
                item = ZhihuActivityItem()
                item.time = int(data.get('created_time'))
                if item.time < after:
                    stop_flag = True
                    break
                item.actor = data.get('actor').get('url_token')
                item.action = data.get('verb')
                target = data.get('target')
                if item.action == 'QUESTION_CREATE' or item.action == 'QUESTION_FOLLOW':  # 关注了问题，添加了问题
                    item.target_user = target.get('author').get('name')
                    item.target_title = target.get('title')
                    item.target_link = 'https://www.zhihu.com/question/{id}'.format(
                        id=target.get('id'))
                elif item.action == 'ANSWER_VOTE_UP' or item.action == 'ANSWER_CREATE':  # 赞同了回答，回答了问题
                    item.target_user = target.get('author').get('name')
                    item.target_title = target.get('question').get('title')
                    item.target_content = target.get('excerpt')
                    item.target_link = 'https://www.zhihu.com/question/{qid}/answer/{aid}'.format(
                        qid=target.get('question').get('id'), aid=target.get('id'))
                elif item.action == 'MEMBER_VOTEUP_ARTICLE' or item.action == 'MEMBER_CREATE_ARTICLE':  # 赞了文章，发表了文章
                    item.target_user = target.get('author').get('name')
                    item.target_title = target.get('title')
                    item.target_content = target.get('excerpt')
                    item.target_link = 'https://zhuanlan.zhihu.com/p/{id}'.format(
                        id=target.get('id'))
                elif item.action == 'TOPIC_FOLLOW' or item.action == 'TOPIC_CREATE':  # 关注了话题，创建了话题
                    item.target_title = target.get('name')
                    item.target_link = 'https://www.zhihu.com/topic/{id}'.format(
                        id=target.get('id'))
                elif item.action == 'MEMBER_FOLLOW_COLUMN' or item.action == 'MEMBER_CREATE_COLUMN':  # 关注了收藏夹，创建了收藏夹
                    item.target_user = target.get('author').get('name')
                    item.target_title = target.get('title')
                    item.target_link = 'https://zhuanlan.zhihu.com/{id}'.format(
                        id=target.get('id'))
                elif item.action == 'MEMBER_CREATE_PIN' or item.action == 'MEMBER_FOLLOW_PIN':  # 发布了想法，关注了想法
                    item.target_user = target.get('author').get('name')
                    item.target_content = target.get('excerpt_new')
                    item.target_link = 'https://www.zhihu.com/pin/{id}'.format(
                        id=target.get('id'))
                activities.append(item)
                if len(activities) >= number:
                    break
            if len(activities) >= number or result.get('paging').get('is_end') or stop_flag:
                break
            response = requests.get(
                zhihu_user_activity_url.format(user=user, limit=10, after=activities[-1].time),
                headers=zhihu_header)
            result = response.json()

        if self._log:
            logging.info('Succeed in scraping activities of zhihu user: %s.' % user)

        return activities

    def scrape_question(self, id=0):
        assert isinstance(id, int), 'Parameter \'id\' should be an instance of type \'int\'!'

        if self._log:
            logging.info('Scraping question of id: %d...' % id)

        response = requests.get(zhihu_question_url.format(id=id, include=zhihu_question_query),
                                    headers=zhihu_header)
        if response.status_code == 404:
            if self._log:
                logging.warning('404 error. The question doesn\'t exist.')
            return None
        result = response.json()

        item = ZhihuQuestionItem()
        item.id = result.get('id')
        item.title = result.get('title')
        item.create_time = int(result.get('created'))
        item.update_time = int(result.get('updated_time'))
        page = requests.get('https://www.zhihu.com/question/%d' % id, headers=zhihu_header)
        bs = BeautifulSoup(page.text, 'lxml')
        content_div = bs.find('div', {'class': 'QuestionRichText'})
        if content_div is not None:
            item.content = re.search(r'<span.*?>(.*)</span>', str(content_div.div.span)).group(1)
        item.follower_count = result.get('follower_count')
        item.visit_count = result.get('visit_count')
        item.comment_count = result.get('comment_count')
        topics = result.get('topics')
        if topics is not None:
            for topic in topics:
                item.topics.append(topic.get('name'))

        if self._log:
            logging.info('Succeed in scraping question of id: %d.' % id)

        self._user_question[id] = item
        return item

    def scrape_user_question(self, user, number=1):
        assert isinstance(user, str), \
            'Parameter \'user\' should be an instance of type \'str\'!'
        assert isinstance(number, int) and number >= 1, \
            'Parameter \'number\' should be an integer which is bigger than 1!'

        if self._log:
            logging.info('Scraping questions of zhihu user: %s...' % user)

        response = requests.get(zhihu_user_question_url.format(user=user, offset=0, limit=20),
                                headers=zhihu_header)
        if response.status_code == 404:  # 用户不存在或账号被封禁
            if self._log:
                logging.warning('404 error. The user doesn\'t exist or has been blocked.')
            return []
        result = response.json()
        total = result.get('paging').get('totals')
        number = min((number, total))
        question_ids = []
        position = 0
        while len(question_ids) < number:
            for data in result.get('data'):
                question_ids.append(data.get('id'))
                if len(question_ids) >= number:
                    break
            if len(question_ids) >= number:
                break
            position += 20
            next_page = zhihu_user_question_url.format(user=user, offset=position, limit=20)
            result = requests.get(next_page, headers=zhihu_header).json()
        questions = []
        for question_id in question_ids:
            item = self.scrape_question(id=question_id)
            questions.append(item)

        if self._log:
            logging.info('Succeed in scraping questions of zhihu user: %s.' % user)

        self._user_question[user] = questions
        return questions

    def scrape_answer(self, id):
        assert isinstance(id, int), \
            'Parameter \'id\' should be an instance of type \'int\'!'

        if self._log:
            logging.info('Scraping answer of id: %d...' % id)

        response = requests.get(zhihu_answer_url.format(id=id, include=zhihu_answer_query),
                                headers=zhihu_header)
        if response.status_code == 404:
            if self._log:
                logging.error('404 error. The answer doesn\'t exist.')
            return None
        if response.status_code == 401:
            if self._log:
                logging.error('401 error. Authentication exception occurred.')
            return None
        result = response.json()
        item = ZhihuAnswerItem()
        item.id = result.get('id')
        item.author = result.get('author').get('name')
        item.question_id = result.get('question').get('id')
        item.create_time = int(result.get('created_time'))
        item.update_time = int(result.get('updated_time'))
        page = requests.get('https://www.zhihu.com/question/%d/answer/%d' % (item.question_id, id),
                            headers=zhihu_header)
        bs = BeautifulSoup(page.text, 'lxml')
        content_span = bs.find('div', {'class': 'RichContent'}).div.span
        content = re.search(r'<span.*?>(.*)</span>', str(content_span)).group(1)
        item.content = content
        item.voteup_count = result.get('voteup_count')
        item.comment_count = result.get('comment_count')

        if self._log:
            logging.info('Succeed in scraping answer of id: %d.' % id)

        self._answer[id] = item
        return item

    def scrape_question_answer(self, id, number=1):
        assert isinstance(id, int), \
            'Parameter \'id\' should be an instance of type \'int\'!'
        assert isinstance(number, int) and number >= 1, \
            'Parameter \'number\' should be an integer which is bigger than 1!'

        if self._log:
            logging.info('Scraping answers of question: %d...' % id)

        response = requests.get(zhihu_question_answer_url.format(id=id, offset=0, limit=20),
                                headers=zhihu_header)
        if response.status_code == 404:  # the question doesn't exist
            if self._log:
                logging.warning('404 error. The question doesn\'t exist.')
            return []
        result = response.json()
        total = result.get('paging').get('totals')
        number = min((number, total))
        answer_ids = []
        while len(answer_ids) < number:
            for data in result.get('data'):
                answer_ids.append(data.get('id'))
                if len(answer_ids) >= number:
                    break
            if len(answer_ids) >= number:
                break
            next_page = result.get('paging').get('next')
            result = requests.get(next_page, headers=zhihu_header).json()
        answers = []
        for answer_id in answer_ids:
            item = self.scrape_answer(id=answer_id)
            answers.append(item)

        if self._log:
            logging.info('Succeed in scraping answers of question: %d.' % id)

        self._question_answer[id] = answers
        return answers

    def scrape_user_answer(self, user, number=1):
        assert isinstance(user, str), \
            'Parameter \'user\' should be an instance of type \'str\'!'
        assert isinstance(number, int) and number >= 1, \
            'Parameter \'number\' should be an integer which is bigger than 1!'

        if self._log:
            logging.info('Scraping answers of zhihu user: %s...' % user)

        response = requests.get(zhihu_user_answer_url.format(user=user, offset=0, limit=20),
                                headers=zhihu_header)
        if response.status_code == 404:  # the user doesn't exist or has been blocked
            if self._log:
                logging.warning('404 error. The user doesn\'t exist or has been blocked.')
            return []
        result = response.json()
        total = result.get('paging').get('totals')
        number = min((number, total))
        answer_ids = []
        position = 0
        while len(answer_ids) < number:
            for data in result.get('data'):
                answer_ids.append(data.get('id'))
                if len(answer_ids) >= number:
                    break
            if len(answer_ids) >= number:
                break
            position += 20
            next_page = zhihu_user_answer_url.format(user=user, offset=position, limit=20)
            result = requests.get(next_page, headers=zhihu_header).json()
        answers = []
        for answer_id in answer_ids:
            item = self.scrape_answer(id=answer_id)
            answers.append(item)

        if self._log:
            logging.info('Succeed in scraping answers of zhihu user: %s.' % user)

        self._user_answer[user] = answers
        return answers

    def save_user_info(self, user=None, directory='./products/'):
        if self._user_info == {}:  # 未爬取过任何用户信息
            if self._log:
                logging.warning('Haven\'t scraped any zhihu user\'s information.')
            return
        if user is None:  # 保存所有爬取过的用户信息
            csv_file = open(directory + 'all-user-info.csv', 'w')
            writer = csv.writer(csv_file)
            writer.writerow(('ID', '用户名', '性别', '头像链接', '行业', '一句话描述', '个人介绍', '提问数', '回答数',
                             '文章数', '被赞同数', '被感谢数', '被收藏数', '关注数', '粉丝数', '关注话题数', '关注专栏数',
                             '关注问题数', '关注收藏夹数', '教育经历', '职业经历', '居住地'))
            for name in self._user_info.keys():
                info = self._user_info.get(name)
                if not isinstance(info, ZhihuUserItem):
                    continue
                if info.sex == 0:
                    gender = '女'
                elif info.sex == 1:
                    gender = '男'
                else:
                    gender = '未知'
                writer.writerow(
                    (info.id, info.name, gender, info.avatar, info.business, info.headline,
                     info.description, info.question_count, info.answer_count, info.article_count,
                     info.voteup_count, info.thanked_count, info.favorited_count,
                     info.following_count,
                     info.follower_count, info.following_topic_count, info.following_column_count,
                     info.following_question_count, info.following_favlist_count,
                     '; '.join([str(edu) for edu in info.educations]),
                     '; '.join([str(emp) for emp in info.employments]),
                     '; '.join([str(loc) for loc in info.locations])))
            csv_file.close()
            if self._log:
                logging.info('Succeed in saving information of all scraped zhihu users.')
            return

        info = self._user_info.get(user)
        assert isinstance(info, ZhihuUserItem), '\'info\' isn\'t an instance of ZhihuUserItem.'
        csv_file = open(directory + str(info.name) + '-info.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(('ID', '用户名', '性别', '头像链接', '行业', '一句话描述', '个人介绍', '提问数', '回答数',
                         '文章数', '被赞同数', '被感谢数', '被收藏数', '关注数', '粉丝数', '关注话题数', '关注专栏数',
                         '关注问题数', '关注收藏夹数', '教育经历', '职业经历', '居住地'))
        if info.sex == 0:
            gender = '女'
        elif info.sex == 1:
            gender = '男'
        else:
            gender = '未知'
        writer.writerow((info.id, info.name, gender, info.avatar, info.business, info.headline,
                         info.description, info.question_count, info.answer_count,
                         info.article_count,
                         info.voteup_count, info.thanked_count, info.favorited_count,
                         info.following_count,
                         info.follower_count, info.following_topic_count,
                         info.following_column_count,
                         info.following_question_count, info.following_favlist_count,
                         '; '.join([str(edu) for edu in info.educations]),
                         '; '.join([str(emp) for emp in info.employments]),
                         '; '.join([str(loc) for loc in info.locations])))
        csv_file.close()
        if self._log:
            logging.info('Succeed in saving information of zhihu user: %s.' % info.name)

    def save_user_following(self, user, directory='./products/'):
        if self._user_following == {}:
            if self._log:
                logging.warning('Haven\'t scraped follows of any zhihu user.')
            return
        infos = self._user_following.get(user)
        assert isinstance(infos, list), 'Haven\'t scraped follows of zhihu user: %s' % user
        csv_file = open(directory + str(user) + '-follows.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(('ID', '用户名', '性别', '头像链接', '行业', '一句话描述', '个人介绍', '提问数', '回答数',
                         '文章数', '被赞同数', '被感谢数', '被收藏数', '关注数', '粉丝数', '关注话题数', '关注专栏数',
                         '关注问题数', '关注收藏夹数', '教育经历', '职业经历', '居住地'))
        for info in infos:
            if not isinstance(info, ZhihuUserItem):
                continue
            if info.sex == 0:
                gender = '女'
            elif info.sex == 1:
                gender = '男'
            else:
                gender = '未知'
            writer.writerow(
                (info.id, info.name, gender, info.avatar, info.business, info.headline,
                 info.description, info.question_count, info.answer_count, info.article_count,
                 info.voteup_count, info.thanked_count, info.favorited_count, info.following_count,
                 info.follower_count, info.following_topic_count, info.following_column_count,
                 info.following_question_count, info.following_favlist_count,
                 '; '.join([str(edu) for edu in info.educations]),
                 '; '.join([str(emp) for emp in info.employments]),
                 '; '.join([str(loc) for loc in info.locations])))
        csv_file.close()
        if self._log:
            logging.info('Succeed in saving follows of zhihu user: %s.' % user)

    def save_user_follower(self, user, directory='./products/'):
        if self._user_follower == {}:
            if self._log:
                logging.warning('Haven\'t scraped followers of any zhihu user.')
            return
        infos = self._user_follower.get(user)
        assert isinstance(infos, list), 'Haven\'t scraped followers of zhihu user: %s' % user
        csv_file = open(directory + str(user) + '-followers.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(('ID', '用户名', '性别', '头像链接', '行业', '一句话描述', '个人介绍', '提问数', '回答数',
                         '文章数', '被赞同数', '被感谢数', '被收藏数', '关注数', '粉丝数', '关注话题数', '关注专栏数',
                         '关注问题数', '关注收藏夹数', '教育经历', '职业经历', '居住地'))
        for info in infos:
            if not isinstance(info, ZhihuUserItem):
                continue
            if info.sex == 0:
                gender = '女'
            elif info.sex == 1:
                gender = '男'
            else:
                gender = '未知'
            writer.writerow(
                (info.id, info.name, gender, info.avatar, info.business, info.headline,
                 info.description, info.question_count, info.answer_count, info.article_count,
                 info.voteup_count, info.thanked_count, info.favorited_count, info.following_count,
                 info.follower_count, info.following_topic_count, info.following_column_count,
                 info.following_question_count, info.following_favlist_count,
                 '; '.join([str(edu) for edu in info.educations]),
                 '; '.join([str(emp) for emp in info.employments]),
                 '; '.join([str(loc) for loc in info.locations])))
        csv_file.close()
        if self._log:
            logging.info('Succeed in saving followers of zhihu user: %s.' % user)
