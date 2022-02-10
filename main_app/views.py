from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Plant

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'
    
class About(TemplateView):
    template_name = 'about.html'
    
class PlantList(TemplateView):
    template_name = 'plant_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        common_name = self.request.GET.get('common_name')

        if common_name != None:
            context['plants'] = Plant.objects.filter(common_name__icontains=common_name)
            context['header'] = f"{common_name.lower().capitalize()} Sightings"
        else:
            context['plants'] = Plant.objects.all()
            context['header'] = "Recent Sightings"
        return context
    
class PlantCreate(CreateView):
    model = Plant
    fields = ['common_name', 'species', 'img', 'city', 'country']
    template_name = 'plant_create.html'
    success_url = '/plants'
    