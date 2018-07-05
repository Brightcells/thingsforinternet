# -*- coding: utf-8 -*-

import datetime
import os
import time

from django.db import models
from django.utils.translation import ugettext_lazy as _
from pysnippets.strsnippets import strip

from accounts.models import UserInfo
from dh.models import FunctionInfo
from thingsforinternet.basemodels import CreateUpdateMixin
from utils.tt4it_utils import *


def upload_path(instance, old_filename):
    extension = os.path.splitext(old_filename)[1].lower()
    today = datetime.datetime.today()
    timestamp = str(time.time())
    file_path = 'resume/{year}{month}/{timestamp}{extension}'.format(
        year=today.year,
        month=today.month,
        timestamp=timestamp,
        extension=extension)
    return file_path


# 简历
class ResumeInfo(CreateUpdateMixin):
    resume = models.TextField(_(u'resume'), blank=True, null=True, help_text=u'resume content which markdown support')
    resume_html = models.TextField(_(u'resume_html'), blank=True, null=True, help_text=u'resume content which html support')
    pdf = models.FileField(_(u'pdf'), upload_to=upload_path, blank=True, null=True, help_text=u'pdf or doc(x)')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'resume tag')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'resume owner')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'是否显示 True for display && False for not')

    class Meta:
        verbose_name = _(u'resumeinfo')
        verbose_name_plural = _(u'resumeinfo')

    @property
    def data(self):
        return {
            'pk': self.pk,
            'resume': self.resume,
            'resume_html': self.resume_html,
            'pdf': self.pdf.url if self.pdf else '',
            'tag': (self.tag or '').split(' '),
            'uid': self.user.pk,
            'uname': self.user.username,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }

    @property
    def info(self):
        return {
            'pk': self.pk,
            'tag': (self.tag or '').split(' '),
            'uid': self.user.pk,
            'uname': self.user.username,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
            'title': strip((self.resume or '').split('\n')[0].split('\r')[0].split('\r\n')[0]),
        }
