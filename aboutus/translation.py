from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('content',)

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('name', 'position')

@register(FinancialReport)
class FinancialReportTranslationOptions(TranslationOptions):
    pass

