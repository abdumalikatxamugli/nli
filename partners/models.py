from django.db import models

# Create your models here.

class PartnerTypes(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title_uz


class Partners(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to='partners')
    partner_type = models.ForeignKey(PartnerTypes, on_delete=models.CASCADE)