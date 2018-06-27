# -*- coding: utf-8 -*-

from django.conf.urls import url

from lab import views as lab_views


urlpatterns = [
    url(r'^$', lab_views.lab, name='lab'),
    url(r'^index/$', lab_views.lab, name='index_lab'),
    url(r'^home/$', lab_views.lab, name='home_lab'),

    url(r'^pinnimei/$', lab_views.pinnimei, name='pinnimei'),
    url(r'^pinnimei/check_word/$', lab_views.check_word, name='check_word'),
]
