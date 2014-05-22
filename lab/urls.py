from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('lab.views',
    url(r'^$', 'lab', name='lab'),
    url(r'^index$', 'lab', name='lab'),
    url(r'^home$', 'lab', name='lab'),

    url(r'^pinnimei$', 'pinnimei', name='pinnimei'),
    url(r'^pinnimei/check_word$', 'check_word', name='check_word'),
)
