from django.db import models

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


