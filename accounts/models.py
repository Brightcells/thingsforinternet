# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


SLIDE_IMAGE_CLASSIFY = (
    ('rx', _(u'RenXiang')),
    ('fj', _(u'FengJing')),
    ('kt', _(u'KaTong')),
    ('bc', _(u'BianCheng')),
    ('dw', _(u'DongWu')),
    ('mx', _(u'MingXing')),
    ('yx', _(u'YouXi')),
    ('zs', _(u'ZheSi')),
)

SEARCH_ENGINE = (
    ('google', _(u'Google')),
    ('stackoverflow', _(u'StackOverflow')),
    ('bing', _(u'Bing')),
    ('tmd', _(u'TMD123')),
    ('baidu', _(u'Baidu')),
    ('tt', _(u'tt4it')),
)


# 用户注册信息表
class UserInfo(models.Model):
    username = models.CharField(_(u'username'), max_length=255, blank=True, null=True, help_text=u'用户名')
    password = models.CharField(_(u'password'), max_length=255, blank=True, null=True, help_text=u'密码')
    email = models.EmailField(_(u'email'), max_length=255, blank=True, null=True, help_text=u'邮箱')
    login_page = models.URLField(_(u'login_page'), max_length=255, blank=True, null=True, help_text=u'登录首页')
    display_bg = models.BooleanField(_('display_bg'), default=True, help_text=u'是否显示背景图')
    classify = models.CharField(_(u'classify'), max_length=255, choices=SLIDE_IMAGE_CLASSIFY, blank=True, null=True, help_text=u'背景图分类')
    search_engine = models.CharField(_(u'search_engine'), max_length=255, choices=SEARCH_ENGINE, blank=True, null=True, help_text=u'默认搜索引擎')
    company = models.CharField(_(u'company'), max_length=255, blank=True, null=True, help_text=u'所在公司')
    github = models.CharField(_(u'github'), max_length=255, blank=True, null=True, help_text='Github')
    sof = models.CharField(_(u'stackoverflow'), max_length=255, blank=True, null=True, help_text='StackOverflow')
    weibo = models.CharField(_(u'weibo'), max_length=255, blank=True, null=True, help_text='Weibo')
    rren = models.CharField(_(u'renren'), max_length=255, blank=True, null=True, help_text='Renren')
    v2ex = models.CharField(_(u'v2ex'), max_length=255, blank=True, null=True, help_text='v2ex')
    blog = models.CharField(_(u'blog'), max_length=255, blank=True, null=True, help_text='Blog')
    btc = models.CharField(_(u'btc'), max_length=255, blank=True, null=True, help_text='btc address')
    freeze = models.BooleanField(_('freeze'), default=False, help_text=u'是否被冻结 True for freeze && False for not freeze')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'注册时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

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
            'login_page': self.login_page,
            'display_bg': self.display_bg,
            'classify': self.classify,
            'search_engine': self.search_engine,
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
