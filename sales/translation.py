from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'slogan', 'description')

@register(ProductPages)
class ProductPagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
