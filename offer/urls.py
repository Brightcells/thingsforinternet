# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('offer.views',
    url(r'^$', 'offer', name='offer'),
    url(r'^index/$', 'offer', name='offer'),
    url(r'^home/$', 'offer', name='offer'),
)
