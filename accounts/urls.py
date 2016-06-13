# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url


urlpatterns = patterns('accounts.views',
    url(r'^$', 'login', name='login'),
    url(r'^index/$', 'login', name='login'),
    url(r'^home/$', 'login', name='login'),

    url(r'^login/$', 'login', name='login'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^forgot/$', 'forgot', name='forgot'),

    url(r'^api_user_check/$', 'api_user_check', name='api_user_check'),
    url(r'^password_reset/$', 'password_reset', name='password_reset'),

    url(r'^member/$', 'member', name='member'),
    url(r'^member/(?P<uid>\d+)/$', 'member', name='member'),
    url(r'^settings/$', 'settings', name='settings'),
)
