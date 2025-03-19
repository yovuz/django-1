from django.db import models

# Create your models here.
class Profile(models.Model):
    # modul cagyrdyk
    username=models.CharField(max_length=100) 
    password=models.CharField(max_length=20) 
    email=models.CharField(max_length=30)  
    age=models.IntegerField() 