from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Smoothie


def home(request):
    smoothies = Smoothie.objects.all()
    context = {
        'smoothies': smoothies
    }
    return render(request, 'smoothies/home.html', context)

class SmoothieListView(ListView):
    model = Smoothie
    template_name = 'smoothies/home.html'
    context_object_name = 'smoothies'

class SmoothieDetailView(DetailView):
    model = Smoothie
    template_name = 'smoothies/smoothie_detail.html'
    context_object_name = 'smoothie'

def about(request):
    return render(request, 'smoothies/about.html')
