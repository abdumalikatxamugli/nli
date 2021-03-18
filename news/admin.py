from django.contrib import admin
from .models import News
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    title = forms.CharField(label="title")
    title_ru = forms.CharField(label='title ru')

    class Meta:
        model = News
        fields = ['title', 'content', 'title_ru']


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title',)

    def save_model(self, request, obj, form, change):
       obj.title=form.cleaned_data.get('title_ru', None)
       super().save_model(request, obj, form, change)

admin.site.register(News, NewsAdmin)
