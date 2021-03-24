from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
# Register your models here.

class ProductPagesForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditorUploadingWidget)
    content_ru = forms.CharField(widget=CKEditorUploadingWidget)
    content_en = forms.CharField(widget=CKEditorUploadingWidget)


class ProductPagesInline(TranslationStackedInline):
    model = ProductPages
    form = ProductPagesForm
    extra = 1

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    inlines = [ProductPagesInline]

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('is_sellable')
            self.exclude.append('selling_form')
        return super(ProductAdmin, self).get_form(request, obj, **kwargs)