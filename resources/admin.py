# -*- coding: utf-8 -*-

from django.contrib import admin

from resources.models import (DIY, ApiInfo, ClassifyInfo, CsySite, Evaluate, Favorite, Like, Log, NavInfo, TagInfo,
                              UserApiInfo, Visit, WebSiteInfo, WebsiteRelatedInfo, WebSiteSubmit)
from utils.qiniucdn import upload


class NavInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('qiniu_image', )
    list_display = ('name', 'title', 'image', 'descr', 'func', 'position', 'display', 'create_time', 'modify_time')
    search_fields = ('name', 'title', 'image', 'descr', 'func__name')
    list_filter = ('func', 'display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'

    def save_model(self, request, obj, form, change):
        obj.qiniu_image = upload(obj.image.read()).get('key', '') if obj.image else ''
        obj.save()


class ClassifyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'descr', 'num', 'visit', 'nav', 'position', 'display', 'create_time', 'modify_time')
    search_fields = ('name', 'title', 'descr')
    list_filter = ('nav', 'display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


class WebSiteInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('qiniu_logo', )
    list_display = ('url', 'name', 'logo', 'slogan', 'descr', 'tag', 'srcode', 'visit', 'evaluate', 'like', 'unlike', 'fav', 'display', 'create_time', 'modify_time')
    search_fields = ('url', 'name', 'logo', 'slogan', 'descr', 'tag', 'srcode')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'

    def save_model(self, request, obj, form, change):
        obj.qiniu_logo = upload(obj.logo.read()).get('key', '') if obj.logo else ''
        obj.save()


class WebsiteRelatedInfoAdmin(admin.ModelAdmin):
    list_display = ('website', 'name', 'url', 'descr', 'srcode', 'display', 'create_time', 'modify_time')
    search_fields = ('name', 'url', 'descr', 'srcode')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'
    raw_id_fields = ('website', )


class TagInfoAdmin(admin.ModelAdmin):
    list_display = ('tag', 'website', 'create_time', 'modify_time')
    search_fields = ('tag', )
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class CsySiteAdmin(admin.ModelAdmin):
    list_display = ('classify', 'website', 'display', 'create_time', 'modify_time')
    search_fields = ('classify__name', 'website__url', 'website__name', 'website__logo', 'website__slogan', 'website__descr', 'website__tag', 'website__srcode')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'
    raw_id_fields = ('classify', )


class EvaluateAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'content', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website', 'content')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'flag', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website', 'flag')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class DIYAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class VisitAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'host', 'website', 'descr', 'create_time', 'modify_time')
    search_fields = ('user', 'host', 'website', 'descr')
    list_filter = ('descr', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


class WebSiteSubmitAdmin(admin.ModelAdmin):
    list_display = ('url', 'tag', 'deal', 'create_time', 'modify_time')
    search_fields = ('url', 'tag', 'deal')
    list_filter = ('deal', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


class ApiInfoAdmin(admin.ModelAdmin):
    list_display = ('api', 'func', 'tag', 'url', 'author', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('api', 'func', 'tag')
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


class UserApiInfoAdmin(admin.ModelAdmin):
    list_display = ('api', 'user', 'status', 'create_time', 'modify_time')
    search_fields = ('api', )
    list_filter = ('create_time', 'modify_time')
    date_hierarchy = 'create_time'


admin.site.register(NavInfo, NavInfoAdmin)
admin.site.register(ClassifyInfo, ClassifyInfoAdmin)
admin.site.register(WebSiteInfo, WebSiteInfoAdmin)
admin.site.register(WebsiteRelatedInfo, WebsiteRelatedInfoAdmin)
admin.site.register(TagInfo, TagInfoAdmin)
admin.site.register(CsySite, CsySiteAdmin)
admin.site.register(Evaluate, EvaluateAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(DIY, DIYAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(WebSiteSubmit, WebSiteSubmitAdmin)

admin.site.register(ApiInfo, ApiInfoAdmin)
admin.site.register(UserApiInfo, UserApiInfoAdmin)
