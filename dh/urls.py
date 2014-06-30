from django.conf.urls import patterns, include, url


urlpatterns = patterns('dh.views',
    url(r'^$', 'dh_home', name='dh_home'),
    url(r'^index$', 'dh', name='dh'),
    url(r'^home$', 'dh', name='dh'),
)
