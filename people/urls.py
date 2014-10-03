from django.conf.urls import patterns, url
import people.views as views

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', views.ClimbsUserDetail.as_view(), name='climbsuser_detail'),
)
