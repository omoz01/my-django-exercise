from django.db import models
#from django.forms import CharField

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100, null=True)
    details = models.CharField(max_length=500, null=True)
