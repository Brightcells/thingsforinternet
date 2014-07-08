# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext

from thingsforinternet.basemodels import CreateUpdateMixin
from accounts.models import UserInfo
from dh.models import FunctionInfo


''' The below models is for ITGPS (技术网站导航) '''


# 网站导航信息表， 其中必然有一个 （school - 学校） 导航， 处理学校相关网站
class NavInfo(models.Model):
    name = models.CharField(_(u'name'), max_length=255, help_text=u'导航名称')
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'导航标题')
    image = models.ImageField(_(u'image'), upload_to='nav', blank=True, null=True, help_text=u'导航图标')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'导航描述')
    func = models.ForeignKey(FunctionInfo, verbose_name=_(u'function'), blank=True, null=True, help_text='Function')
    position = models.IntegerField(_(u'position'), blank=True, null=True, default=0, help_text=u'导航位置')
    display = models.BooleanField(_('display'), default=True, help_text=u'导航是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'navinfo'
        verbose_name = _(u'navinfo')
        verbose_name_plural = _(u'navinfo')

    def __unicode__(self):
        return unicode(self.title)


# 网站导航分类信息表
class ClassifyInfo(models.Model):
    name = models.CharField(_(u'name'), max_length=255, help_text=u'分类名称')
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'分类标题')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'分类描述')
    num = models.IntegerField(_(u'num'), default=0, help_text=u'分类站点数')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'分类站点点击数')
    nav = models.ForeignKey(NavInfo, verbose_name=_(u'nav'), blank=True, null=True, help_text=u'分类所属导航')
    position = models.IntegerField(_(u'position'), default=0, help_text=u'分类位置')
    display = models.BooleanField(_('display'), default=True, help_text=u'分类是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'classifyinfo'
        verbose_name = _(u'classifyinfo')
        verbose_name_plural = _(u'classifyinfo')

    def __unicode__(self):
        return unicode(self.title)

    def _data(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'title': self.title,
            'descr': self.descr,
            'num': self.num,
            'visit': self.visit,
            'nav': self.nav,
        }

    data = property(_data)


# 网站信息表
class WebSiteInfo(models.Model):
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'网站网址')
    name = models.CharField(_(u'name'), max_length=255, blank=True, null=True, help_text=u'网站名称')
    logo = models.ImageField(_(u'image'), upload_to='logo', blank=True, null=True, help_text=u'网站 logo')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'网站描述')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'网站标签')
    srcode = models.CharField(_(u'srcode'), max_length=255, blank=True, null=True, help_text=u'网站源码')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'网站访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'网站评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'网站点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'网站被踩数')
    fav = models.IntegerField(_(u'fav'), default=0, help_text=u'网站收藏数')
    display = models.BooleanField(_('display'), default=True, help_text=u'网站是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'websiteinfo'
        verbose_name = _(u'websiteinfo')
        verbose_name_plural = _(u'websiteinfo')

    def __unicode__(self):
        return unicode(self.url)

    def _data(self):
        return {
            'pk': self.pk,
            'url': self.url,
            'name': self.name,
            'logo': self.logo.url if self.logo else '',
            'descr': self.descr,
            'tag': self.tag,
            'srcode': self.srcode,
            'visit': self.visit,
            'like': self.like,
            'unlike': self.unlike,
            'fav': self.fav,
        }

    data = property(_data)


# 网站相关信息表
class WebsiteRelatedInfo(models.Model):
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='related_website', help_text=u'网站')
    name = models.CharField(_(u'name'), max_length=255, blank=True, null=True, help_text=u'网站相关信息名称')
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'网站相关信息网址')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'网站相关信息描述')
    srcode = models.CharField(_(u'srcode'), max_length=255, blank=True, null=True, help_text=u'网站相关信息源码')
    display = models.BooleanField(_('display'), default=True, help_text=u'网站相关信息是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'websiterelatedinfo'
        verbose_name = _(u'websiterelatedinfo')
        verbose_name_plural = _(u'websiterelatedinfo')

    def __unicode__(self):
        return unicode(self.website)


# 网站标签信息表
class TagInfo(models.Model):
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'网站网址')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='taginfo_website', help_text=u'网站')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'taginfo'
        verbose_name = _(u'taginfo')
        verbose_name_plural = _(u'taginfo')

    def __unicode__(self):
        return unicode(self.tag)


# 网站导航分类 -- 网站
class CsySite(models.Model):
    classify = models.ForeignKey(ClassifyInfo, verbose_name=_(u'classify'), blank=True, null=True, help_text=u'网站导航分类')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='csysite_website', help_text=u'网站')
    display = models.BooleanField(_(u'display'), default=True, help_text=u'网站是否显示 True for display && False for not')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'csysite'
        verbose_name = _(u'csysite')
        verbose_name_plural = _(u'csysite')

    def __unicode__(self):
        return unicode(self.pk)

    def _data(self):
        return {
            'pk': self.pk,
            'classify': self.classify,
            'website': self.website.data,
        }

    data = property(_data)


# 评价记录表
class Evaluate(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户， blank=True代表陌生人评论')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text=u'评论 IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='evaluate_website', help_text=u'网站')
    content = models.TextField(_(u'content'), blank=True, null=True, help_text=u'用户评价内容')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'evaluate'
        verbose_name = _(u'evaluate')
        verbose_name_plural = _(u'evaluate')

    def __unicode__(self):
        return unicode(self.pk)


# 赞/踩记录表
class Like(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户， blank=True 代表陌生人赞/踩')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text=u'赞/踩IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='like_website', help_text=u'网站')
    flag = models.BooleanField(_('flag'), default=True, help_text=u'赞 or 踩 True for like && False for unlike')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'like'
        verbose_name = _(u'like')
        verbose_name_plural = _(u'like')

    def __unicode__(self):
        return unicode(self.pk)


# 收藏记录表
class Favorite(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text=u'收藏 IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='favorite_website', help_text=u'网站')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'favorite'
        verbose_name = _(u'favorite')
        verbose_name_plural = _(u'favorite')

    def __unicode__(self):
        return unicode(self.pk)

    def _data(self):
        return {
            'pk': self.pk,
            'user': self.user,
            'host': self.host,
            'website': self.website.data,
        }

    data = property(_data)


# DIY 记录表
class DIY(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text=u'收藏 IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='diy_website', help_text=u'网站')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        verbose_name = _(u'diy')
        verbose_name_plural = _(u'diy')

    def __unicode__(self):
        return unicode(self.pk)

    def _data(self):
        return {
            'pk': self.pk,
            'user': self.user,
            'host': self.host,
            'website': self.website.data,
        }

    data = property(_data)


# 访问记录表
class Visit(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text=u'访问 IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='visit_website', help_text=u'网站')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'visit'
        verbose_name = _(u'visit')
        verbose_name_plural = _(u'visit')

    def __unicode__(self):
        return unicode(self.pk)


# 统一 Log 记录表
class Log(models.Model):
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    host = models.GenericIPAddressField(_('host'), max_length=20, blank=True, null=True, help_text='IP')
    website = models.ForeignKey(WebSiteInfo, verbose_name=_(u'website'), blank=True, null=True, related_name='log_website', help_text=u'网站')
    descr = models.TextField(_('description'), blank=True, null=True, help_text=u'Log 描述')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'log'
        verbose_name = _(u'log')
        verbose_name_plural = _(u'log')

    def __unicode__(self):
        return unicode(self.pk)


# 站点提交记录表
class WebSiteSubmit(models.Model):
    url = models.CharField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'网站网址')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'网站标签')
    deal = models.BooleanField(_('deal'), default=False, help_text=u'网站提交是否已处理 True for deal && False for not')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'websitesubmit'
        verbose_name = _(u'websitesubmit')
        verbose_name_plural = _(u'websitesubmit')

    def __unicode__(self):
        return unicode(self.url)


''' The below models is for API '''


# API 信息表
class ApiInfo(CreateUpdateMixin):
    api = models.CharField(_(u'api'), max_length=255, blank=True, null=True, help_text=u'API 名称')
    func = models.TextField(_(u'function'), blank=True, null=True, help_text=u'API  功能描述')
    tag = models.CharField(_(u'tag'), max_length=255, blank=True, null=True, help_text=u'API 标签')
    url = models.URLField(_(u'url'), max_length=255, blank=True, null=True, help_text=u'API 详细信息')
    author = models.ForeignKey(UserInfo, verbose_name=_(u'author'), blank=True, null=True, help_text=u'API 创建者')
    visit = models.IntegerField(_(u'visit'), default=0, help_text=u'API 访问数')
    evaluate = models.IntegerField(_(u'evaluate'), default=0, help_text=u'API 评价数')
    like = models.IntegerField(_(u'like'), default=0, help_text=u'API 点赞数')
    unlike = models.IntegerField(_(u'unlike'), default=0, help_text=u'API 被踩数')
    follow = models.IntegerField(_(u'follow'), default=0, help_text=u'API 关注数')
    display = models.BooleanField(_('display'), default=True, help_text=u'API 是否显示 True for display && False for not')

    class Meta:
        db_table = u'apiinfo'
        verbose_name = _(u'apiinfo')
        verbose_name_plural = _(u'apiinfo')

    def __unicode__(self):
        return unicode(self.api)

    def _data(self):
        return {
            'pk': self.pk,
            'api': self.api,
            'func': self.func,
            'tag': self.tag.split(' '),
            'url': self.url,
            'visit': self.visit,
            'like': self.like,
            'follow': self.follow,
        }

    data = property(_data)


# 用户 - API 信息表
class UserApiInfo(CreateUpdateMixin):
    api = models.ForeignKey(ApiInfo, verbose_name=_(u'api'), blank=True, null=True, help_text=u'API')
    user = models.ForeignKey(UserInfo, verbose_name=_(u'user'), blank=True, null=True, help_text=u'用户')
    status = models.BooleanField(_('status'), default=True, help_text=u'API 是否为自己创建 True for create && False for follow')

    class Meta:
        db_table = u'userapiinfo'
        verbose_name = _(u'userapiinfo')
        verbose_name_plural = _(u'userapiinfo')

    def __unicode__(self):
        return unicode(self.api)