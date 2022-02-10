from django.db import models

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)