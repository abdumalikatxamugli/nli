from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(ResourceType)
class ResourceTypeAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(Resource)
class ResourceAdmin(TranslationAdmin):
    list_display = ('title',)
