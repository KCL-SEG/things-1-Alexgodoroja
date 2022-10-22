from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models import Model
class Thing(Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
