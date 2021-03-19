from django.contrib import admin
from .models import News
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import mark_safe


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    title = forms.CharField(label="title")
    short_content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mytextarea'}
    ))

    class Meta:
        model = News
        fields = ['title', 'short_content', 'content', 'category', 'image']


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('title', 'short_content', 'thumb')

    def thumb(self, obj):
        return mark_safe("<img width='200px' src=/uploads/" + str(obj.image) + "/>")

    thumb.allow_tags = True
    thumb.__name__ = 'Thumb'


admin.site.register(News, NewsAdmin)
