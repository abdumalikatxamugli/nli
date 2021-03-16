from django.db import models


def defaultMultiLang():
    return {
        'uz': '',
        'ru': '',
        'en': ''
    }


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'news'
