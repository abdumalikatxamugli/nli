from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(PartnerTypes)
class PartnerTypesTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



