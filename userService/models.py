from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    logo = models.TextField(default='mongrol.svg', null=True)
    wallet = models.IntegerField(default=0)
    color = models.CharField(max_length=7, default='#FF6666')
    telegramName = models.CharField(max_length=7, null=True)
    status = models.TextField(null=True)

