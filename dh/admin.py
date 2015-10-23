# -*- coding: utf-8 -*-

from django.contrib import admin

from dh.models import AppInfo, FunctionInfo


class AppInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'image', 'descr', 'position', 'display', 'create_time', 'modify_time')


class FunctionInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'image', 'descr', 'app', 'position', 'display', 'create_time', 'modify_time')


admin.site.register(AppInfo, AppInfoAdmin)
admin.site.register(FunctionInfo, FunctionInfoAdmin)
