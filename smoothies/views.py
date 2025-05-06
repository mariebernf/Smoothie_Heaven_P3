from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'smoothies/home.html')


def about(request):
    return render(request, 'smoothies/about.html')
