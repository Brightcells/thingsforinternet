from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('resume.views',
    url(r'^$', 'resume', name='resume'),
    url(r'^index$', 'resume', name='resume'),
    url(r'^home$', 'resume', name='resume'),
)
