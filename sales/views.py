from django.shortcuts import render

# Create your views here.
from .models import Sale

from django.http import HttpResponse

def index(request):
    # return HttpResponse('Hi')
    data=Sale.objects.all()
    return render(request, 'sale.html',{'sales':data})