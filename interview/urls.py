# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url


urlpatterns = patterns('interview.views',
    url(r'^$', 'interview', name='interview'),
    url(r'^index/$', 'interview', name='interview'),
    url(r'^home/$', 'interview', name='interview'),
)
