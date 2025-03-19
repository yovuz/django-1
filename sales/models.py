from django.db import models

# Create your models here.

class Sale(models.Model):
    price=models.IntegerField()
    definition=models.CharField(max_length=255)
    # modeldan son migrate etmeli