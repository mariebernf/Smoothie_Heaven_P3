from django.urls import path
from . import views

'app/model_viewtype'
'smoothies/smoothie_detail.html'

urlpatterns = [
    path('', views.SmoothieListView.as_view(), name="smoothies-home"),
    path('<int:pk>/', views.SmoothieDetailView.as_view(), name="smoothies-detail"),
    path('about/', views.about, name="about"),  
]
