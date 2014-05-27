from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('accounts.views',
    url(r'^$', 'login', name='login'),
    url(r'^index$', 'login', name='login'),
    url(r'^home$', 'login', name='login'),
    url(r'^login$', 'login', name='login'),
    url(r'^signup$', 'signup', name='signup'),
    url(r'^logout$', 'logout', name='logout'),
    url(r'^api_user_check$', 'api_user_check', name='api_user_check'),
)
