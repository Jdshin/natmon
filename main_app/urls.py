from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about', views.About.as_view(), name='about'),
    path('plants', views.PlantList.as_view(), name='plant_list'),
    path('plants/new', views.PlantCreate.as_view(), name='plant_create'),
]
