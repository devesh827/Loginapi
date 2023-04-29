from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=10,default='',unique=True,)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    mobile=models.IntegerField(default=1)

   