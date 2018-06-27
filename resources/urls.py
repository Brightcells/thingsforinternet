# -*- coding: utf-8 -*-

from django.conf.urls import url

from resources import views as resources_views


urlpatterns = [
    url(r'^$', resources_views.resources, name='resources'),
    url(r'^index/$', resources_views.resources, name='index_resources'),
    url(r'^home/$', resources_views.resources, name='home_resources'),

    url(r'^itgps/keyboard/$', resources_views.itgpskeyboard, name='itgpskeyboard'),

    url(r'^itgps/home/$', resources_views.itgpshome, name='itgpshome'),
    url(r'^itgps/home/(?P<p>\d+)/$', resources_views.itgpshome, name='itgpshome'),
    url(r'^itgps/fav/$', resources_views.itgpsfav, name='itgpsfav'),
    url(r'^itgps/fav/(?P<p>\d+)/$', resources_views.itgpsfav, name='itgpsfav'),
    url(r'^itgps/diy/$', resources_views.itgpsdiy, name='itgpsdiy'),
    url(r'^itgps/hottest_lastest/$', resources_views.itgps_hottest_lastest, name='itgps_hottest_lastest'),
    url(r'^itgps/hot/$', resources_views.itgpshot, name='itgpshot'),
    url(r'^itgps/hot/(?P<p>\d+)/$', resources_views.itgpshot, name='itgpshot'),
    url(r'^itgps/last/$', resources_views.itgpslast, name='itgpslast'),
    url(r'^itgps/last/(?P<p>\d+)/$', resources_views.itgpslast, name='itgpslast'),
    url(r'^csysite/(?P<pk>\d+)/$', resources_views.csysite, name='csysite'),
    url(r'^csysite/(?P<pk>\d+)/(?P<p>\d+)/$', resources_views.csysite, name='csysite'),
    url(r'^visit/$', resources_views.visit, name='visit'),
    url(r'^favorite/$', resources_views.favorite, name='favorite'),
    url(r'^discuss/(?P<siteid>\d+)/$', resources_views.discuss, name='discuss'),
    url(r'^like/$', resources_views.like, name='like'),
    url(r'^itgps/favlike/(?P<siteid>\d+)/$', resources_views.itgpsfavlike, name='itgpsfavlike'),
    url(r'^itgps/search/$', resources_views.itgpssearch, name='itgpssearch'),
    url(r'^itgps/search/(?P<p>\d+)/$', resources_views.itgpssearch, name='itgpssearch'),
    url(r'^itgps/submit/$', resources_views.itgpssubmit, name='itgpssubmit'),
    url(r'^itgps/submit/(?P<p>\d+)/$', resources_views.itgpssubmit, name='itgpssubmit'),
    url(r'^itgps/(?P<_nav>\w+)/$', resources_views.itgps, name='itgps'),

    url(r'^api/home/$', resources_views.apihome, name='apihome'),
    url(r'^api/record/$', resources_views.apirecord, name='apirecord'),
    url(r'^api/record/(?P<p>\d+)/$', resources_views.apirecord, name='apirecord'),
    url(r'^api/mine/$', resources_views.apimine, name='apimine'),
    url(r'^api/mine/(?P<p>\d+)/$', resources_views.apimine, name='apimine'),
    url(r'^api/all/$', resources_views.apiall, name='apiall'),
    url(r'^api/all/(?P<p>\d+)/$', resources_views.apiall, name='apiall'),
    url(r'^api/discuss/(?P<aid>\d+)/$', resources_views.apidiscuss, name='apidiscuss'),
    url(r'^api/search/$', resources_views.apisearch, name='apisearch'),
    url(r'^api/search/(?P<p>\d+)/$', resources_views.apisearch, name='apisearch'),

    url(r'^software/home/$', resources_views.softwarehome, name='softwarehome'),
]
