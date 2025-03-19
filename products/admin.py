from django.contrib import admin
# Register your models here.
from .models import Product
# admin diyen model icinden adminmodel ulanyas
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')
admin.site.register(Product,ProductAdmin)