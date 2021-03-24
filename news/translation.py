from modeltranslation.translator import register, TranslationOptions
from .models import *

@register
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_content', 'content')

@register
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)