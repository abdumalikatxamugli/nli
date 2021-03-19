from django.db import models


# Create your models here.

class History(models.Model):
    years = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to='history', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company History"


class Certificate(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='certificates', null=True)
    file = models.FileField(upload_to='certificates', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Certificates"


class Management(models.Model):
    name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    image = models.ImageField(upload_to='management', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Management"

class FinancialReport(models.Model):
    year = models.CharField(max_length=4)
    file = models.FileField(upload_to='financial_reports', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Financial Reports"
