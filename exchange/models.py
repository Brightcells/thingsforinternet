# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from thingsforinternet.basemodels import CreateUpdateMixin
from accounts.models import UserInfo
from dh.models import FunctionInfo

from utils.utils import *


# 知识便签
class Tips(CreateUpdateMixin):
    tips = models.TextField(_(u'tips'), blank=True, null=True, help_text=u'知识便签 名称')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'知识便签 标签')
    url = models.URLField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'知识便签 网址')
    author = models.ForeignKey(UserInfo, verbose_name=_(u'author'), blank=True, null=True, help_text=u'API 创建者')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'知识便签 访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'知识便签 评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'知识便签 点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'知识便签 被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'知识便签 关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'知识便签 是否显示 True for display && False for not')

    class Meta:
        db_table = u'tips'
        verbose_name = _(u'tips')
        verbose_name_plural = _(u'tips')

    def _data(self):
        return {
            'pk': self.pk,
            'tips': self.tips,
            'tag': self.tag.split(' '),
            'url': self.url,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }

    data = property(_data)


# 用户 - 知识便签
class UserTips(CreateUpdateMixin):
    tips = models.ForeignKey(Tips, verbose_name=_(u'tips'), blank=True, null=True, help_text=u'知识便签')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    status = models.BooleanField(_('status'), default=True, help_text=u'知识便签 是否为自己创建 True for create && False for follow')

    class Meta:
        db_table = u'usertips'
        verbose_name = _(u'usertips')
        verbose_name_plural = _(u'usertips')

    def __unicode__(self):
        return unicode(self.tips)


# 博客
class BlogInfo(CreateUpdateMixin):
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'博客 标题')
    blog = models.TextField(_(u'blog'), blank=True, null=True, help_text=u'博客 内容')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'博客 标签')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'author'), blank=True, null=True, help_text=u'博客 作者')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'博客 访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'博客 评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'博客 点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'博客 被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'博客 关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'博客 是否显示 True for display && False for not')

    class Meta:
        verbose_name = _(u'bloginfo')
        verbose_name_plural = _(u'bloginfo')

    def _data(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'blog': self.blog,
            'tag': self.tag.split(' '),
            'uname': self.user.username,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }

    data = property(_data)


# 博客精选
class BlogSelectedInfo(CreateUpdateMixin):
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'博客精选 标题')
    url = models.URLField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'博客精选 网址')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'博客精选 标签')
    author = models.CharField(_(u'author'), max_length=255, blank=True, null=True, help_text=u'博客精选 作者')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'author'), blank=True, null=True, help_text=u'博客精选 创建者')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'博客精选 访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'博客精选 评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'博客精选 点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'博客精选 被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'博客精选 关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'博客精选 是否显示 True for display && False for not')

    class Meta:
        verbose_name = _(u'blogselectedinfo')
        verbose_name_plural = _(u'blogselectedinfo')

    def _data(self):
        return {
            'pk': self.pk,
            'title': self.title,
            'url': self.url,
            'tag': self.tag.split(' '),
            'author': self.author,
            'uname': self.user.username,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }

    data = property(_data)
