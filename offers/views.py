from django.shortcuts import render

from .models import Offer

from django.http import HttpResponse
# ulanyjy gecdi gormane diymek


def index(request):
# default sahypa
    # return HttpResponse("Welcome to products page")
    offers=Offer.objects.all()   # hemme product alyp beryar
    return render(request,'offers.html',{'offers':offers})  # ulanyja acyp beryar render