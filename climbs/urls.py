from django.conf.urls import patterns, url
import climbs.views as views

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', views.ClimbDetail.as_view(), name='climb_detail'),
    url(r'^(?P<pk>\d+)/rate/$', views.ClimbRate.as_view(), name='climb_rate'),
)
