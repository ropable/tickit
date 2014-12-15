from django.conf.urls import patterns, url, include
from rest_framework import routers
import people.views as views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^(?P<pk>\d+)/$', views.ClimbsUserDetail.as_view(), name='climbsuser_detail'),
)
