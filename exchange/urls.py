from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('exchange.views',
    url(r'^$', 'exchange', name='exchange'),
    url(r'^index/$', 'exchange', name='exchange'),
    url(r'^home/$', 'exchange', name='exchange'),

    url(r'^tips/home/$', 'tipshome', name='tipshome'),
    url(r'^tips/record/$', 'tipsrecord', name='tipsrecord'),
    url(r'^tips/record/(?P<p>\d+)/$', 'tipsrecord', name='tipsrecord'),
    url(r'^tips/mine/$', 'tipsmine', name='tipsmine'),
    url(r'^tips/mine/(?P<p>\d+)/$', 'tipsmine', name='tipsmine'),
    url(r'^tips/all/$', 'tipsall', name='tipsall'),
    url(r'^tips/all/(?P<p>\d+)/$', 'tipsall', name='tipsall'),
    url(r'^tips/discuss/(?P<pk>\d+)/$', 'tipsdiscuss', name='tipsdiscuss'),
    url(r'^tips/search/$', 'tipssearch', name='tipssearch'),
    url(r'^tips/search/(?P<p>\d+)/$', 'tipssearch', name='tipssearch'),

    url(r'^forum/home/$', 'forumhome', name='forumhome'),

    url(r'^blog/home/$', 'bloghome', name='bloghome'),
    url(r'^blog/record/$', 'blogrecord', name='blogrecord'),
    url(r'^blog/record/(?P<p>\d+)/$', 'blogrecord', name='blogrecord'),
    url(r'^blog/mine/$', 'blogmine', name='blogmine'),
    url(r'^blog/mine/(?P<p>\d+)/$', 'blogmine', name='blogmine'),
    url(r'^blog/all/$', 'blogall', name='blogall'),
    url(r'^blog/all/(?P<p>\d+)/$', 'blogall', name='blogall'),
    url(r'^blog/edit/$', 'blogedit', name='blogedit'),
    url(r'^blog/edit/(?P<pk>\d+)/$', 'blogedit', name='blogedit'),
    url(r'^blog/discuss/(?P<pk>\d+)/$', 'blogdiscuss', name='blogdiscuss'),
    url(r'^blog/discuss2/(?P<pk>\d+)/$', 'blogdiscuss2', name='blogdiscuss2'),
    url(r'^blog/search/$', 'blogsearch', name='blogsearch'),
    url(r'^blog/search/(?P<p>\d+)/$', 'blogsearch', name='blogsearch'),

    url(r'^blog/selected/$', 'blogselected', name='blogselected'),
    url(r'^blog/selected/(?P<p>\d+)/$', 'blogselected', name='blogselected'),
)
