from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUsers(AbstractUser):
     UserID = models.AutoField(primary_key=True)
     def __str__(self):
        return self.username
