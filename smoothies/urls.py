from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmoothieListView.as_view(), name="smoothies-home"),
    path('about/', views.about, name="smoothies-about"),
    path('create/', views.SmoothieCreateView.as_view(), name="smoothies-create"),
    path('<int:pk>/', views.SmoothieDetailView.as_view(), name="smoothies-detail"),
]
