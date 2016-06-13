# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('resume.views',
    url(r'^$', 'resume', name='resume'),
    url(r'^index/$', 'resume', name='resume'),
    url(r'^home/$', 'resume', name='resume'),

    url(r'^resume2/home/$', 'resume2home', name='resume2home'),
    url(r'^resume2/all/$', 'resume2all', name='resume2all'),
    url(r'^resume2/all/(?P<p>\d+)/$', 'resume2all', name='resume2all'),
    url(r'^resume2/mine/$', 'resume2mine', name='resume2mine'),
    url(r'^resume2/edit/$', 'resume2edit', name='resume2edit'),
    url(r'^resume2/discuss/(?P<uid>\d+)/$', 'resume2discuss', name='resume2discuss'),
    url(r'^resume2/discuss2/(?P<uid>\d+)/$', 'resume2discuss2', name='resume2discuss2'),
    url(r'^resume2/search/$', 'resume2search', name='resume2search'),
    url(r'^resume2/search/(?P<p>\d+)/$', 'resume2search', name='resume2search'),
)
