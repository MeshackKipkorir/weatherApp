from django.db import models

# Create your models here.
class weatherModel(models.Model):
    name = models.CharField(blank=True, max_length=50)
