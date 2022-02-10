from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class PlantList(TemplateView):
    template_name = 'plantList.html'