from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url('^help/$', TemplateView.as_view(template_name='index.html'), name='help'),
    url('^$', TemplateView.as_view(template_name='index.html'), name='home'),
)
