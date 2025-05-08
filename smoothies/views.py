from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


def home(request):
    smoothies = models.Smoothie.objects.all()
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

class SmoothieCreateView(LoginRequiredMixin, CreateView):
    model = models.Smoothie
    fields = ['name', 'description', 'ingredients']
    template_name = 'smoothies/smoothie_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'smoothies/about.html')
