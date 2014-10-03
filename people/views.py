from django.views.generic import DetailView
from .models import ClimbsUser


class ClimbsUserDetail(DetailView):
    model = ClimbsUser
    template_name = 'people/climbsuser_detail.html'
