from django.contrib import admin
# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=('kod','total_price','quantity')
admin.site.register(Order,OrderAdmin)