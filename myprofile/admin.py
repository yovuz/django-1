from django.contrib import admin
# Register your models here.
from .models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display=('username','password','email','age')
admin.site.register(Profile,ProfileAdmin)