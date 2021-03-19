from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

class HistoryAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

class HistoryAdmin(admin.ModelAdmin):
    form = HistoryAdminForm
    list_display = ('years',)


admin.site.register(History, HistoryAdmin)


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Certificate, CertificateAdmin)


class ManagementAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Management, ManagementAdmin)


class FinancialReportsAdmin(admin.ModelAdmin):
    list_display = ('year',)


admin.site.register(FinancialReport, FinancialReportsAdmin)