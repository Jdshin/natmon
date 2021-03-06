from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Plant
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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
    
class PlantDetail(DetailView):
    model = Plant
    template_name = 'plant_detail.html'
    
class PlantUpdate(UpdateView):
    model = Plant
    fields = ['common_name', 'species', 'img', 'city', 'country']
    template_name = 'plant_update.html'
    success_url = '/plants'
    
class PlantDelete(DeleteView):
    model = Plant
    template_name = 'plant_delete.html'
    success_url = '/url'

class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': 'form'}
        return render(request, 'registration/signup.html', context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('artist_list')
        else:
            context = {'form':form}
            return render(request, 'registration/signup.html', context)
        
        