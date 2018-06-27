# -*- coding: utf-8 -*-

from django.conf.urls import url

from exchange import views as exchange_views


urlpatterns = [
    url(r'^$', exchange_views.exchange, name='exchange'),
    url(r'^index/$', exchange_views.exchange, name='index_exchange'),
    url(r'^home/$', exchange_views.exchange, name='home_exchange'),

    url(r'^tips/home/$', exchange_views.tipshome, name='tipshome'),
    url(r'^tips/record/$', exchange_views.tipsrecord, name='tipsrecord'),
    url(r'^tips/record/(?P<p>\d+)/$', exchange_views.tipsrecord, name='tipsrecord'),
    url(r'^tips/mine/$', exchange_views.tipsmine, name='tipsmine'),
    url(r'^tips/mine/(?P<p>\d+)/$', exchange_views.tipsmine, name='tipsmine'),
    url(r'^tips/all/$', exchange_views.tipsall, name='tipsall'),
    url(r'^tips/all/(?P<p>\d+)/$', exchange_views.tipsall, name='tipsall'),
    url(r'^tips/discuss/(?P<pk>\d+)/$', exchange_views.tipsdiscuss, name='tipsdiscuss'),
    url(r'^tips/search/$', exchange_views.tipssearch, name='tipssearch'),
    url(r'^tips/search/(?P<p>\d+)/$', exchange_views.tipssearch, name='tipssearch'),

    url(r'^forum/home/$', exchange_views.forumhome, name='forumhome'),

    url(r'^blog/home/$', exchange_views.bloghome, name='bloghome'),
    url(r'^blog/record/$', exchange_views.blogrecord, name='blogrecord'),
    url(r'^blog/record/(?P<p>\d+)/$', exchange_views.blogrecord, name='blogrecord'),
    url(r'^blog/mine/$', exchange_views.blogmine, name='blogmine'),
    url(r'^blog/mine/(?P<p>\d+)/$', exchange_views.blogmine, name='blogmine'),
    url(r'^blog/all/$', exchange_views.blogall, name='blogall'),
    url(r'^blog/all/(?P<p>\d+)/$', exchange_views.blogall, name='blogall'),
    url(r'^blog/edit/$', exchange_views.blogedit, name='blogedit'),
    url(r'^blog/edit/(?P<pk>\d+)/$', exchange_views.blogedit, name='blogedit'),
    url(r'^blog/discuss/(?P<pk>\d+)/$', exchange_views.blogdiscuss, name='blogdiscuss'),
    url(r'^blog/discuss2/(?P<pk>\d+)/$', exchange_views.blogdiscuss2, name='blogdiscuss2'),
    url(r'^blog/search/$', exchange_views.blogsearch, name='blogsearch'),
    url(r'^blog/search/(?P<p>\d+)/$', exchange_views.blogsearch, name='blogsearch'),

    url(r'^blog/selected/$', exchange_views.blogselected, name='blogselected'),
    url(r'^blog/selected/(?P<p>\d+)/$', exchange_views.blogselected, name='blogselected'),
]
