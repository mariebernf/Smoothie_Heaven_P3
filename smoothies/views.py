from django.shortcuts import render
from .models import Smoothie 


def home(request):
    smoothies = Smoothie.objects.all()
    context = {
        'smoothies': smoothies
    }
    return render(request, 'smoothies/home.html', context)


def about(request):
    return render(request, 'smoothies/about.html')
