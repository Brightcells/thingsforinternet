# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


# 用户注册信息表
class UserInfo(models.Model):
    username = models.CharField(_(u'username'), max_length=255, blank=True, null=True)  # 用户名称
    password = models.CharField(_(u'password'), max_length=255, blank=True, null=True)  # 用户密码
    email = models.EmailField(_(u'email'), max_length=255, blank=True, null=True)  # 用户邮箱
    company = models.EmailField(_(u'company'), max_length=255, blank=True, null=True)  # 用户所在公司
    github = models.CharField(_(u'github'), max_length=255, blank=True, null=True)  # 用户 Github
    sof = models.CharField(_(u'stackoverflow'), max_length=255, blank=True, null=True)  # 用户 stackoverflow
    weibo = models.CharField(_(u'weibo'), max_length=255, blank=True, null=True)  # 用户 weibo
    rren = models.CharField(_(u'renren'), max_length=255, blank=True, null=True)  # 用户 renren
    v2ex = models.CharField(_(u'v2ex'), max_length=255, blank=True, null=True)  # 用户 v2ex
    blog = models.CharField(_(u'blog'), max_length=255, blank=True, null=True)  # 用户 blog
    btc = models.CharField(_(u'btc'), max_length=255, blank=True, null=True)  # 用户 btc address
    freeze = models.BooleanField(_('freeze'), default=False)  # 用户是否被冻结 True for freeze && False for not freeze
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True)  # 用户注册时间
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True)  # 用户修改时间

    class Meta:
        db_table = u'userinfo'
        verbose_name = _(u'userinfo')
        verbose_name_plural = _(u'userinfo')

    def __unicode__(self):
        return unicode(self.username)

    def _data(self):
        return {
            'pk': self.pk,
            'username': self.username,
            'email': self.email,
            'company': self.company,
            'github': self.github,
            'sof': self.sof,
            'weibo': self.weibo,
            'rren': self.rren,
            'v2ex': self.v2ex,
            'blog': self.blog,
            'btc': self.btc,
            'create_time': self.create_time.replace(tzinfo=None),
        }

    data = property(_data)
