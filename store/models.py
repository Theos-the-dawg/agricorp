from django.db import models
from datetime import datetime

class Harvest(models.Model):
    crop = models.CharField(max_length=50)
    crops = models.JSONField()
    date_harvested= models.DateField(default=datetime.now())

def __str__(self):
    return self.crop