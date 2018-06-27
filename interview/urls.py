# -*- coding: utf-8 -*-

from django.conf.urls import url

from interview import views as interview_views


urlpatterns = [
    url(r'^$', interview_views.interview, name='interview'),
    url(r'^index/$', interview_views.interview, name='index_interview'),
    url(r'^home/$', interview_views.interview, name='home_interview'),
]
