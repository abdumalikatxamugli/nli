from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsCategory(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title_uz

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=256)
    short_content = models.CharField(max_length=512)
    content = models.TextField()
    image = models.ImageField(upload_to='news', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Новости'
        db_table = 'news'


