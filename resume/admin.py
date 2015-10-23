# -*- coding: utf-8 -*-

from django.contrib import admin

from resume.models import ResumeInfo


class ResumeInfoAdmin(admin.ModelAdmin):
    list_display = ('resume', 'pdf', 'tag', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('resume', 'resume_html', 'pdf', 'tag')
    list_filter = ('display', 'create_time', 'modify_time')
    date_hierarchy = 'create_time'


admin.site.register(ResumeInfo, ResumeInfoAdmin)
