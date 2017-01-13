# -*- coding: utf-8 -*-

import datetime
import os
import time

from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserInfo
from thingsforinternet.basemodels import CreateUpdateMixin
from utils.tt4it_utils import *


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'huntjob/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


# 面试题
class QuestionInfo(CreateUpdateMixin):
    question = models.TextField(_(u'question'), blank=True, null=True, help_text=u'面试题 题目')
    answer = models.TextField(_(u'answer'), blank=True, null=True, help_text=u'面试题 答案')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'面试题 标签')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'面试题 上传者')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'是否显示 True for display && False for not')

    class Meta:
        verbose_name = _(u'questioninfo')
        verbose_name_plural = _(u'questioninfo')

    @property
    def data(self):
        return {
            'pk': self.pk,
            'question': self.question,
            'answer': self.answer,
            'tag': self.tag.split(' '),
            'uid': self.user.pk,
            'uname': self.user.username,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }
