from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Branch)
class BranchTypesTranslationOptions(TranslationOptions):
    fields = ('title', 'address')




