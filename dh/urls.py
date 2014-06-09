from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('dh.views',
    url(r'^$', 'dh_home', name='dh_home'),
    url(r'^index$', 'dh', name='dh'),
    url(r'^home$', 'dh', name='dh'),
)
