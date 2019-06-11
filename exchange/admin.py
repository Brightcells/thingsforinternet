# -*- coding: utf-8 -*-

from django.contrib import admin

from exchange.models import BlogInfo, BlogSelectedInfo, Tips, UserTips


class TipsAdmin(admin.ModelAdmin):
    list_display = ('tips', 'tag', 'url', 'author', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('tips', 'tag', 'url')
    list_filter = ('display', 'create_time', 'modify_time')


class UserTipsAdmin(admin.ModelAdmin):
    list_display = ('tips', 'user', 'status', 'create_time', 'modify_time')
    search_fields = ('tips', 'user')
    list_filter = ('status', 'create_time', 'modify_time')


class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog', 'tag', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('title', 'blog', 'tag')
    list_filter = ('display', 'create_time', 'modify_time')


class BlogSelectedInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'tag', 'author', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('title', 'tag', 'author')
    list_filter = ('display', 'create_time', 'modify_time')


admin.site.register(Tips, TipsAdmin)
admin.site.register(UserTips, UserTipsAdmin)
admin.site.register(BlogInfo, BlogInfoAdmin)
admin.site.register(BlogSelectedInfo, BlogSelectedInfoAdmin)
