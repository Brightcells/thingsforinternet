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

    url(r'^software/home$', 'softwarehome', name='softwarehome'),
)
