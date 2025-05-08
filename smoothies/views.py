from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Smoothie

from . import models


def home(request):
    smoothies = Smoothie.objects.all()
    context = {
        'smoothies': smoothies
    }
    return render(request, 'smoothies/home.html', context)

class SmoothieListView(ListView):
    model = models.Smoothie
    template_name = 'smoothies/home.html'
    context_object_name = 'smoothies'

class SmoothieDetailView(DetailView):
    model = models.Smoothie
    template_name = 'smoothies/smoothie_detail.html'
    context_object_name = 'object'

class SmoothieCreateView(CreateView):
    model = models.Smoothie
    fields = ['name', 'description', 'ingredients', 'author']
    template_name = 'smoothies/smoothie_form.html'
    success_url = '/'

def about(request):
    return render(request, 'smoothies/about.html')
