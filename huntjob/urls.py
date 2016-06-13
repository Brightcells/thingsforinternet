# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('huntjob.views',
    url(r'^$', 'huntjob', name='huntjob'),
    url(r'^index/$', 'huntjob', name='huntjob'),
    url(r'^home/$', 'huntjob', name='huntjob'),

    url(r'^question/home/$', 'questionhome', name='questionhome'),
    url(r'^question/record/$', 'questionrecord', name='questionrecord'),
    url(r'^question/record/(?P<p>\d+)/$', 'questionrecord', name='questionrecord'),
    url(r'^question/all/$', 'questionall', name='questionall'),
    url(r'^question/all/(?P<p>\d+)/$', 'questionall', name='questionall'),
    url(r'^question/mine/$', 'questionmine', name='questionmine'),
    url(r'^question/edit/$', 'questionedit', name='questionedit'),
    url(r'^question/discuss/(?P<qid>\d+)/$', 'questiondiscuss', name='questiondiscuss'),
    url(r'^question/search/$', 'questionsearch', name='questionsearch'),
    url(r'^question/search/(?P<p>\d+)/$', 'questionsearch', name='questionsearch'),
)
