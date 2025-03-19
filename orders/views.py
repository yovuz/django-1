from django.shortcuts import render

from .models import Order
# Create your views here.

from django.http import HttpResponse
# ulanyjy gecdi gormane diymek


def index(request):
# default sahypa
    # return HttpResponse("Welcome to orders page")
    orders=Order.objects.all()
    return render(request,'index2.html',{'orders':orders})