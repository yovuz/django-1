from django.contrib import admin

# Register your models here.
from .models import Offer
# admin diyen model icinden adminmodel ulanyas
class OfferAdmin(admin.ModelAdmin):
    list_display=('like','dislike')
admin.site.register(Offer,OfferAdmin)