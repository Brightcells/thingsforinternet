# -*- coding: utf-8 -*-

from django.conf.urls import url

from huntjob import views as huntjob_views


urlpatterns = [
    url(r'^$', huntjob_views.huntjob, name='huntjob'),
    url(r'^index/$', huntjob_views.huntjob, name='index_huntjob'),
    url(r'^home/$', huntjob_views.huntjob, name='home_huntjob'),

    url(r'^question/home/$', huntjob_views.questionhome, name='questionhome'),
    url(r'^question/record/$', huntjob_views.questionrecord, name='questionrecord'),
    url(r'^question/record/(?P<p>\d+)/$', huntjob_views.questionrecord, name='questionrecord'),
    url(r'^question/all/$', huntjob_views.questionall, name='questionall'),
    url(r'^question/all/(?P<p>\d+)/$', huntjob_views.questionall, name='questionall'),
    url(r'^question/mine/$', huntjob_views.questionmine, name='questionmine'),
    url(r'^question/edit/$', huntjob_views.questionedit, name='questionedit'),
    url(r'^question/discuss/(?P<qid>\d+)/$', huntjob_views.questiondiscuss, name='questiondiscuss'),
    url(r'^question/search/$', huntjob_views.questionsearch, name='questionsearch'),
    url(r'^question/search/(?P<p>\d+)/$', huntjob_views.questionsearch, name='questionsearch'),
]
