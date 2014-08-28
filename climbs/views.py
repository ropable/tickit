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
    template_name = 'climb_detail.html'


class RatingCreate(CreateView):
    model = Rating
    template_name = 'rating_create.html'
