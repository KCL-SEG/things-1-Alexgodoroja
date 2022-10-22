from django.db import models
from django.core.exceptions import ValidationError

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120)
    quantity = models.IntegerField()
    if quantity<0 or quantity>100:
        raise ValidationError('Start date is after end date')