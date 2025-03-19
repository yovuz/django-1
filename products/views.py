from django.shortcuts import render
#render bn template ugradyp bole

from .models import Product

from django.http import HttpResponse
# ulanyjy gecdi gormane diymek


def index(request):
# default sahypa
    # return HttpResponse("Welcome to products page")
    products=Product.objects.all()   # hemme product alyp beryar
    return render(request,'index.html',{'products':products})  # ulanyja acyp beryar render