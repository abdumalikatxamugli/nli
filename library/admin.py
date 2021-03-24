from django.contrib import admin
from .models import *
# Register your models here.

class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceType, ResourceTypeAdmin)