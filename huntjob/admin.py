# -*- coding: utf-8 -*-

from django.contrib import admin

from huntjob.models import QuestionInfo


class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'tag', 'user', 'visit', 'evaluate', 'like', 'unlike', 'follow', 'display', 'create_time', 'modify_time')
    search_fields = ('question', 'answer', 'tag')
    list_filter = ('display', 'create_time', 'modify_time')


admin.site.register(QuestionInfo, QuestionInfoAdmin)
