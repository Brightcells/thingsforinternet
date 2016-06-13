# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('lab.views',
    url(r'^$', 'lab', name='lab'),
    url(r'^index/$', 'lab', name='lab'),
    url(r'^home/$', 'lab', name='lab'),

    url(r'^pinnimei/$', 'pinnimei', name='pinnimei'),
    url(r'^pinnimei/check_word/$', 'check_word', name='check_word'),
)
