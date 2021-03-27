from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin


# Register your models here.

class HistoryAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())


@admin.register(History)
class HistoryAdmin(TranslationAdmin):
    form = HistoryAdminForm
    list_display = ('years',)


@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(Management)
class ManagementAdmin(TranslationAdmin):
    list_display = ('name',)


class FinancialReportsAdminForm(forms.ModelForm):
    content_uz = forms.CharField(widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(widget=CKEditorUploadingWidget())
    content_en = forms.CharField(widget=CKEditorUploadingWidget())


@admin.register(FinancialReport)
class FinancialReportsAdmin(TranslationAdmin):
    form = FinancialReportsAdminForm
    list_display = ('year',)
