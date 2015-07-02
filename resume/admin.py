from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from resume.models import *


class ResumeInfoAdmin(admin.ModelAdmin):
    list_display = ('resume', 'pdf', 'tag', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('resume', 'resume_html', 'pdf', 'tag')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


admin.site.register(ResumeInfo, ResumeInfoAdmin)
