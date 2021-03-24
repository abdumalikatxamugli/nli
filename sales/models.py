from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    slogan = models.CharField(max_length=512)
    description = models.TextField()
    is_sellable = models.BooleanField()
    selling_form = models.CharField(max_length=256)


class ProductPages(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)