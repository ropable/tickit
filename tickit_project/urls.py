from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Next line is to remove the logout confirmation step.
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),
    (r'^users/', include('people.urls')),
    (r'^', include('pages.urls')),
    (r'^', include('climbs.urls')),
)

# Additional URLS for development/debug.
if settings.DEBUG:
    # Add in Debug Toolbar URLs.
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
