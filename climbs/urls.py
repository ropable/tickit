from django.conf.urls import patterns, url
from .views import ClimbDetail

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', ClimbDetail.as_view(), name='climb_detail'),
)
