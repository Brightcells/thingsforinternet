# -*- coding: utf-8 -*-

from django.contrib import admin

from accounts.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'login_page', 'display_bg', 'classify', 'search_engine', 'company', 'github', 'sof', 'weibo', 'rren', 'v2ex', 'blog', 'btc', 'freeze', 'create_time', 'modify_time')


admin.site.register(UserInfo, UserInfoAdmin)
