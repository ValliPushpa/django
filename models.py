from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import datetime

class Container(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField()
    upvote=models.PositiveIntegerField(default = 0)
    downvote=models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(default = datetime.datetime.now())