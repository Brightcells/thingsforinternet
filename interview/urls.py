from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('interview.views',
    url(r'^$', 'interview', name='interview'),
    url(r'^index$', 'interview', name='interview'),
    url(r'^home$', 'interview', name='interview'),
)
