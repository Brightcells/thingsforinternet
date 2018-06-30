# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from thingsforinternet import views as tt4it_views


admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'thingsforinternet.views.home', name='home'),
    # url(r'^thingsforinternet/', include('thingsforinternet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^', include('dh.urls', namespace='dh')),
    # url(r'^dh/', include('dh.urls', namespace='dh')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^resume/', include('resume.urls', namespace='resume')),
    url(r'^huntjob/', include('huntjob.urls', namespace='huntjob')),
    url(r'^interview/', include('interview.urls', namespace='interview')),
    url(r'^offer/', include('offer.urls', namespace='offer')),
    url(r'^exchange/', include('exchange.urls', namespace='exchange')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^lab/', include('lab.urls', namespace='lab')),
]

urlpatterns += [
    url(r'^search/$', tt4it_views.search, name='search'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# AdminSite
admin.site.site_header = '［TT4IT］优质互联网资源整合分享平台'
