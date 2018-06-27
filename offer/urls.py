# -*- coding: utf-8 -*-

from django.conf.urls import url

from offer import views as offer_views


urlpatterns = [
    url(r'^$', offer_views.offer, name='offer'),
    url(r'^index/$', offer_views.offer, name='index_offer'),
    url(r'^home/$', offer_views.offer, name='home_offer'),
]
