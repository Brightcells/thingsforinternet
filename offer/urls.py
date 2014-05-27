from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('offer.views',
    url(r'^$', 'offer', name='offer'),
    url(r'^index$', 'offer', name='offer'),
    url(r'^home$', 'offer', name='offer'),
)
