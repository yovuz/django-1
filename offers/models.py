from django.db import models

# Create your models here.
class Offer(models.Model):
    # modul cagyrdyk
    like=models.IntegerField() #column   string bolana charfield
    dislike=models.IntegerField() #column   double san