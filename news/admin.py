from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import mark_safe
from modeltranslation.admin import TranslationAdmin

class NewsAdminForm(forms.ModelForm):
    content_uz = forms.CharField(label='Описание[uz]', widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(label='Описание[ru]', widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label='Описание[en]', widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    list_display = ('title_uz', 'short_content_uz', 'thumb')

    def thumb(self, obj):
        return mark_safe("<img width='200px' src=/uploads/" + str(obj.image) + "/>")

    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'


@admin.register(NewsCategory)
class NewsCategoryAdmin(TranslationAdmin):
    list_display = ('title_uz', )
