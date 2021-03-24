from django.db import models

# Create your models here.

class ResourceType(models.Model):
    title = models.CharField(max_length=512)

    def __str__(self):
        return self.title

class Resource(models.Model):
    title = models.CharField(max_length=512)
    file = models.FileField(upload_to='library/code')
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Ресурсы'


