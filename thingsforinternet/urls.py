from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thingsforinternet.views.home', name='home'),
    # url(r'^thingsforinternet/', include('thingsforinternet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^', include('dh.urls', namespace='dh')),
    url(r'^dh/', include('dh.urls', namespace='dh')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^resume/', include('resume.urls', namespace='resume')),
    url(r'^huntjob/', include('huntjob.urls', namespace='huntjob')),
    url(r'^interview/', include('interview.urls', namespace='interview')),
    url(r'^offer/', include('offer.urls', namespace='offer')),
    url(r'^exchange/', include('exchange.urls', namespace='exchange')),
    url(r'^resources/', include('resources.urls', namespace='resources')),
    url(r'^lab/', include('lab.urls', namespace='lab')),
)

# This is set for media url
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

# urlpatterns += patterns('',
#     url(r'^media/(?P<path>.*)', 'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# )

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('thingsforinternet.views',
    url(r'^search$', 'search', name='search'),
)