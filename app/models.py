from django.db import models

# Create your models here.
class fruits(models.Model):
    fruits = models.CharField(max_length=25)
    region = models.CharField(max_length=30)

class region(models.Model):
    name = models.CharField(max_length=25)