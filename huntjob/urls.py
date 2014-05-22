from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('huntjob.views',
    url(r'^$', 'huntjob', name='huntjob'),
    url(r'^index$', 'huntjob', name='huntjob'),
    url(r'^home$', 'huntjob', name='huntjob'),
)
