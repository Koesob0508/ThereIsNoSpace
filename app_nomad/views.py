from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from app_nomad.models import Region, Coworking, Accommodation
from django.shortcuts import render, redirect, get_object_or_404
from app_nomad.forms import PostCoworking, PostAccommodation

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

#-- Funcion
def coworking_new(request):
    if request.method == "POST":
        form = PostCoworking(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('nomad:coworking_detail', pk=post.pk)
    else:
        form = PostCoworking()
    return render(request, 'app_nomad/coworking_edit.html', {'form':form})

def coworking_edit(request, pk):
    post = get_object_or_404(Coworking, pk=pk)
    if request.method == "POST":
        form = PostCoworking(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('nomad:coworking_detail', pk=post.pk)
    else:
        form = PostCoworking(instance=post)
    return render(request, 'app_nomad/coworking_edit.html', {'form':form})

def accommodation_new(request):
    if request.method == "POST":
        form = PostAccommodation(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('nomad:accommodation_detail', pk=post.pk)
    else:
        form = PostAccommodation()
    return render(request, 'app_nomad/accommodation_edit.html', {'form':form})

def accommodation_edit(request, pk):
    post = get_object_or_404(Accommodation, pk=pk)
    if request.method == "POST":
        form = PostAccommodation(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('nomad:accommodation_detail', pk=post.pk)
    else:
        form = PostAccommodation(instance=post)
    return render(request, 'app_nomad/accommodation_edit.html', {'form':form})
