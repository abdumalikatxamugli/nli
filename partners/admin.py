from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(PartnerTypes)
class PartnerTypesAdmin(TranslationAdmin):
    list_display = ('title_uz',)


class PartnersAdminForm(forms.ModelForm):
    content_uz = forms.CharField(label='Описание[uz]', widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(label='Описание[ru]', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Описание[en]', widget=CKEditorUploadingWidget())


@admin.register(Partners)
class PartnersAdmin(TranslationAdmin):
    form = PartnersAdminForm
    list_display = ('title_uz',)
