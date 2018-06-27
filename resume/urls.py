# -*- coding: utf-8 -*-

from django.conf.urls import url

from resume import views as resume_views


urlpatterns = [
    url(r'^$', resume_views.resume, name='resume'),
    url(r'^index/$', resume_views.resume, name='index_resume'),
    url(r'^home/$', resume_views.resume, name='home_resume'),

    url(r'^resume2/home/$', resume_views.resume2home, name='resume2home'),
    url(r'^resume2/all/$', resume_views.resume2all, name='resume2all'),
    url(r'^resume2/all/(?P<p>\d+)/$', resume_views.resume2all, name='resume2all'),
    url(r'^resume2/mine/$', resume_views.resume2mine, name='resume2mine'),
    url(r'^resume2/edit/$', resume_views.resume2edit, name='resume2edit'),
    url(r'^resume2/discuss/(?P<uid>\d+)/$', resume_views.resume2discuss, name='resume2discuss'),
    url(r'^resume2/discuss2/(?P<uid>\d+)/$', resume_views.resume2discuss2, name='resume2discuss2'),
    url(r'^resume2/search/$', resume_views.resume2search, name='resume2search'),
    url(r'^resume2/search/(?P<p>\d+)/$', resume_views.resume2search, name='resume2search'),
]
