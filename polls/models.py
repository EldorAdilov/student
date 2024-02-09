from django.db import models
from users.models import MyUseer

# Create your models here.

class Vote(models.Model):
    user = models.OneToOneField(MyUseer, on_delete=models.CASCADE)
    to_democrats = models.BooleanField(default=False)

class Video(models.Model):
    objects = None
    name = models.CharField(max_length=64)
    image = models.FileField(upload_to='videolar/')