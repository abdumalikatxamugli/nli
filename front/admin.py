from django.contrib import admin
from .models import News
from modeltranslation.admin import TranslationAdmin
# Register your models here.



@admin.register(News)
class NewsAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            "fields": (("title", "description"))
        }),
    )

