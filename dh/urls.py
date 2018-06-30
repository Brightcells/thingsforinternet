# -*- coding: utf-8 -*-

from django.conf.urls import url

from dh import views as dh_views


urlpatterns = [
    url(r'^$', dh_views.dh3, name='dh'),
    # url(r'^index/$', dh_views.dh3, name='index_dh'),
    # url(r'^home/$', dh_views.dh3, name='home_dh'),
]
