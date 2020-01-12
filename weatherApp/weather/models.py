from django.db import models

# Create your models here.
class weatherModel(models.Model):
    name = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "cities"