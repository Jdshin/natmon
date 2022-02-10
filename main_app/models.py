from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100, blank=True, default='')
    img = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
