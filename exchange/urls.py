from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('exchange.views',
    url(r'^$', 'exchange', name='exchange'),
    url(r'^index$', 'exchange', name='exchange'),
    url(r'^home$', 'exchange', name='exchange'),

    url(r'^tips/home$', 'tipshome', name='tipshome'),
    url(r'^tips/record$', 'tipsrecord', name='tipsrecord'),
    url(r'^tips/record/(?P<p>\d+)/$', 'tipsrecord', name='tipsrecord'),
    url(r'^tips/mine$', 'tipsmine', name='tipsmine'),
    url(r'^tips/mine/(?P<p>\d+)/$', 'tipsmine', name='tipsmine'),
    url(r'^tips/all$', 'tipsall', name='tipsall'),
    url(r'^tips/all/(?P<p>\d+)/$', 'tipsall', name='tipsall'),
    url(r'^discuss/(?P<tipid>\d+)/$', 'discuss', name='discuss'),
    url(r'^tips/search$', 'tipssearch', name='tipssearch'),
    url(r'^tips/search/(?P<p>\d+)/$', 'tipssearch', name='tipssearch'),

    url(r'^forum/home$', 'forumhome', name='forumhome'),
)
