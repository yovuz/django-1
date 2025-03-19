from django.db import models

# Create your models here.
class Order(models.Model):
    # modul cagyrdyk
    kod=models.CharField(max_length=20) #column   string bolana charfield
    total_price=models.FloatField() #column   double san
    quantity=models.IntegerField() #column  integer 