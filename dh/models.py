# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


# 项目 APP 信息表
class AppInfo(models.Model):
    name = models.CharField(_(u'name'), max_length=255, help_text=u'APP 名称')
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'APP 标题')
    image = models.ImageField(_(u'image'), upload_to='app', blank=True, null=True, help_text=u'APP 图标')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'APP 描述')
    position = models.IntegerField(_(u'position'), blank=True, null=True, default=0, help_text=u'APP 位置')
    display = models.BooleanField(_('display'), default=True, help_text=u'APP 是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'appinfo'
        verbose_name = _(u'appinfo')
        verbose_name_plural = _(u'appinfo')

    def __unicode__(self):
        return unicode(self.title)


# APP 功能信息表
class FunctionInfo(models.Model):
    name = models.CharField(_(u'name'), max_length=255, help_text=u'APP 功能名称')
    title = models.CharField(_(u'title'), max_length=255, blank=True, null=True, help_text=u'APP 功能标题')
    image = models.ImageField(_(u'image'), upload_to='function', blank=True, null=True, help_text=u'APP 功能图标')
    descr = models.TextField(_(u'description'), blank=True, null=True, help_text=u'APP 功能描述')
    app = models.ForeignKey(AppInfo, verbose_name=_(u'app'), blank=True, null=True, help_text=u'APP')
    position = models.IntegerField(_(u'position'), blank=True, null=True, default=0, help_text=u'APP 功能位置')
    display = models.BooleanField(_('display'), default=True, help_text=u'APP 功能是否显示 True for display && False for not display')
    create_time = models.DateTimeField(_(u'createtime'), auto_now_add=True, editable=True, help_text=u'添加时间')
    modify_time = models.DateTimeField(_(u'modifytime'), auto_now=True, editable=True, help_text=u'修改时间')

    class Meta:
        db_table = u'functioninfo'
        verbose_name = _(u'functioninfo')
        verbose_name_plural = _(u'functioninfo')

    def __unicode__(self):
        return unicode(self.title)

    def _data(self):
        return {
            'pk': self.pk,
            'name': self.name.lower(),
            'title': self.title,
            'image': self.image.url if self.image else '',
            'descr': self.descr,
        }

    data = property(_data)
