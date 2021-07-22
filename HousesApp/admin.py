from django.contrib import admin
from .models import HouseListing, HouseCompartment

# Register your models here.

class HouseListingAdmin(admin.ModelAdmin):
	list_display = ('nome_do_proprietario','preço','cidade','distrito','bairro','data_registrada')
	list_filter = ('data_registrada','cidade', 'distrito', 'bairro')

admin.site.register(HouseListing,HouseListingAdmin)
admin.site.register(HouseCompartment)