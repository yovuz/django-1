from django.contrib import admin

# Register your models here.

from .models import Sale
class SaleAdmin(admin.ModelAdmin):
    list_display=('price','definition')

admin.site.register(Sale,SaleAdmin)