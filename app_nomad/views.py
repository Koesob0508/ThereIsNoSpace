from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from app_nomad.models import Region, Coworking, Accommodation
from django.shortcuts import render

# Create your views here.

#-- TemplateView
class IndexView(TemplateView):
    template_name = 'app_nomad/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Region', 'Coworking', 'Accommodation']
        return context

#-- ListView
class RegionList(ListView):
    model = Region

class CoworkingList(ListView):
    model = Coworking

class AccommodationList(ListView):
    model = Accommodation

#-- DetailView
class RegionDetail(DetailView):
    model = Region

class CoworkingDetail(DetailView):
    model = Coworking

class AccommodationDetail(DetailView):
    model = Accommodation
