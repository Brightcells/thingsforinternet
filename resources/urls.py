from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('resources.views',
    url(r'^$', 'resources', name='resources'),
    url(r'^index$', 'resources', name='resources'),
    url(r'^home$', 'resources', name='resources'),

    url(r'^itgps/home$', 'itgpshome', name='itgpshome'),
    url(r'^itgps/(?P<_nav>\w+)/$', 'itgps', name='itgps'),
    url(r'^csysite/(?P<_id>\d+)/$', 'csysite', name='csysite'),
    url(r'^visit$', 'visit', name='visit'),
    url(r'^favorite$', 'favorite', name='favorite'),
    url(r'^discuss/(?P<siteid>\d+)/$', 'discuss', name='discuss'),
    url(r'^like$', 'like', name='like'),
    url(r'^itgps/search$', 'itgpssearch', name='itgpssearch'),
    url(r'^itgps/submit$', 'itgpssubmit', name='itgpssubmit'),
    url(r'^itgps/submit/(?P<p>\d+)/$', 'itgpssubmit', name='itgpssubmit'),

    url(r'^api/home$', 'apihome', name='apihome'),
    url(r'^api/record$', 'apirecord', name='apirecord'),
    url(r'^api/record/(?P<p>\d+)/$', 'apirecord', name='apirecord'),
    url(r'^api/mine$', 'apimine', name='apimine'),
    url(r'^api/mine/(?P<p>\d+)/$', 'apimine', name='apimine'),
    url(r'^api/all$', 'apiall', name='apiall'),
    url(r'^api/all/(?P<p>\d+)/$', 'apiall', name='apiall'),
    url(r'^api/discuss/(?P<aid>\d+)/$', 'apidiscuss', name='apidiscuss'),
    url(r'^api/search$', 'apisearch', name='apisearch'),
    url(r'^api/search/(?P<p>\d+)/$', 'apisearch', name='apisearch'),

    url(r'^software/home$', 'softwarehome', name='softwarehome'),
)
