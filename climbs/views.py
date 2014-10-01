from django.views.generic import CreateView, DetailView
from .models import Business, Climb, Rating


class BusinessCreate(CreateView):
    model = Business
    template_name = 'business_create.html'


class BusinessDetail(DetailView):
    model = Business
    template_name = 'business_detail.html'


class ClimbDetail(DetailView):
    model = Climb
    template_name = 'climbs/climb_detail.html'


class ClimbRate(CreateView):
    model = Rating
    template_name = 'climbs/climb_rate.html'
