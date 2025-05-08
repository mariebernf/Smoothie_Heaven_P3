from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Models

class Smoothie(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    author = models.CharField(max_length=50)
    date_posted = models.DateField(auto_now_add=True)

    
    def __str__(self):
       return self.name
    
    def get_absolute_url(self):
        return reverse('smoothies-detail', kwargs={'pk': self.pk})
