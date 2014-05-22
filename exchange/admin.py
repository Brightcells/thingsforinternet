from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from exchange.models import *


class TipsAdmin(admin.ModelAdmin):
    list_display = ('tips', 'tag', 'url', 'author', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('tips', 'tag', 'url')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


class UserTipsAdmin(admin.ModelAdmin):
    list_display = ('tips', 'user', 'status', 'create_time', 'modify_time')
    search_fields = ('tips', 'user')
    list_filter = ('status', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


admin.site.register(Tips, TipsAdmin)
admin.site.register(UserTips, UserTipsAdmin)
