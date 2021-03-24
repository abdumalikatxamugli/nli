from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_content', 'content')

@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)