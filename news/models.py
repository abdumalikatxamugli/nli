from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=256)
    short_content = models.CharField(max_length=512)
    content = models.TextField()
    class Category(models.TextChoices):
        COMPANY = 'COMPANY', _('КОМПАНИЯ')
        ABOUT_US = 'ABOUT_US', _('О НАС')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='Новости'
        db_table='news'