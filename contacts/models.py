from django.db import models
from treasuremap.fields import LatLongField
# Create your models here.

class Branch(models.Model):
    title = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    phone_number = models.CharField(max_length=14)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = LatLongField(blank = True)
