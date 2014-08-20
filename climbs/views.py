from django.views.generic import DetailView
from .models import Climb


class ClimbDetail(DetailView):
    model = Climb
    template_name = 'climb_detail.html'
