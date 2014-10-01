from django.conf.urls import patterns, url
import climbs.views as views

urlpatterns = patterns(
    '',
    # Climb-related views
    url(r'^climb/(?P<pk>\d+)/$', views.ClimbDetail.as_view(), name='climb_detail'),
    url(r'^climb/(?P<pk>\d+)/rate/$', views.ClimbRate.as_view(), name='climb_rate'),
    # Business-related views
    url(r'^business/create/$', views.BusinessCreate.as_view(), name='business_create'),
    url(r'^business/(?P<slug>[\w-]+)/$', views.BusinessDetail.as_view(), name='business_detail'),
)
