from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(ResourceType)
class ResourceTypeOptions(TranslationOptions):
    fields = ('title',)

@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('title',)


