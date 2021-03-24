from django.contrib import admin
from .models import *
# Register your models here.

class PartnerTypesAdmin(admin.ModelAdmin):
    list_display = ('title',)

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Partners, PartnersAdmin)
admin.site.register(PartnerTypes, PartnerTypesAdmin)