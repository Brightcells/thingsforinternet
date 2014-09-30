from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from huntjob.models import *


class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'tag', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('question', 'answer', 'tag')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


admin.site.register(QuestionInfo, QuestionInfoAdmin)
