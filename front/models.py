from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'news'
