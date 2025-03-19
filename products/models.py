from django.db import models

# Create your models here.
class Product(models.Model):
    # modul cagyrdyk
    name=models.CharField(max_length=255) #column   string bolana charfield
    price=models.FloatField() #column   double san
    stock=models.IntegerField() #column  integer 