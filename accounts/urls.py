# -*- coding: utf-8 -*-

from django.conf.urls import url

from accounts import views as accounts_views


urlpatterns = [
    url(r'^$', accounts_views.login, name='login'),
    url(r'^index/$', accounts_views.login, name='index_login'),
    url(r'^home/$', accounts_views.login, name='home_login'),

    url(r'^login/$', accounts_views.login, name='login_login'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^forgot/$', accounts_views.forgot, name='forgot'),

    url(r'^api_user_check/$', accounts_views.api_user_check, name='api_user_check'),
    url(r'^password_reset/$', accounts_views.password_reset, name='password_reset'),

    url(r'^member/$', accounts_views.member, name='member'),
    url(r'^member/(?P<uid>\d+)/$', accounts_views.member, name='member'),
    url(r'^settings/$', accounts_views.settings, name='settings'),
]
