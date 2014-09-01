from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from accounts.models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'login_page', 'display_bg', 'classify', 'company', 'github', 'sof', 'weibo', 'rren', 'v2ex', 'blog', 'btc', 'freeze', 'create_time', 'modify_time')


admin.site.register(UserInfo, UserInfoAdmin)
