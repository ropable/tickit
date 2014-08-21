from django.views.generic import DetailView, FormView
from .models import Climb


class ClimbDetail(DetailView):
    model = Climb
    template_name = 'climb_detail.html'


class ClimbRate(FormView):
    model = Climb
    template_name = 'climb_rate.html'
