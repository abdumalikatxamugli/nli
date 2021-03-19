from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class News(models.Model):
    class Category(models.TextChoices):
        COMPANY = 'COMPANY', _('КОМПАНИЯ')
        ABOUT_US = 'ABOUT_US', _('О НАС')

    title = models.CharField(max_length=256)
    short_content = models.CharField(max_length=512)
    content = models.TextField()
    image = models.ImageField(upload_to='news', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=128,
        choices=Category.choices,
        default=Category.COMPANY
    )

    class Meta:
        verbose_name_plural = 'Новости'
        db_table = 'news'


