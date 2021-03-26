from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=256)
    slogan = models.CharField(max_length=512)
    description = models.TextField()
    is_sellable = models.BooleanField(default=False)
    selling_form = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='uploads/products', blank=True)

    def __str__(self):
        return self.title_uz


class ProductPages(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)