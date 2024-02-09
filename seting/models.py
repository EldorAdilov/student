from django.db import models

# Create your models here.
# models.py


class Person(models.Model):
    objects = None
    familya = models.CharField(max_length=50)
    ism = models.CharField(max_length=50)

