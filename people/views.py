from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from rest_framework import viewsets
from .models import ClimbsUser
from .serializers import UserSerializer


class ClimbsUserDetail(DetailView):
    model = ClimbsUser
    template_name = 'people/climbsuser_detail.html'


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
