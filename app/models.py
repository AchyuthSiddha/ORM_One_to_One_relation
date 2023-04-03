from django.db import models

# Create your models here.
from app.models import *

class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)

class Capital(models.Model):
    captial_name=models.ForeignKey(Country,on_delete=models.CASCADE)

