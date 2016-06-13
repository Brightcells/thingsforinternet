# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('dh.views',
    url(r'^$', 'dh3', name='dh_home'),
    url(r'^index/$', 'dh3', name='dh'),
    url(r'^home/$', 'dh3', name='dh'),

    # url(r'^home2/$', 'dh2', name='dh2'),
    # url(r'^home3/$', 'dh3', name='dh3'),
)
