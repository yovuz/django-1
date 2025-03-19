from django.shortcuts import render

from .models import Profile  # model icindaki Order

# Create your views here.
from django.http import HttpResponse
# ulanyjy gecdi gormane diymek


def index(request):
# default sahypa
    # return HttpResponse("Welcome to profile")
    datas=Profile.objects.all()
    return render(request,'index3.html',{'profiles':datas})
                                         # 'key': value