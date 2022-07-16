from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(default = "01000000000", max_length=11, blank=True)
    is_email_open = models.IntegerField(default=0)
    is_phone_open = models.IntegerField(default=0)
    
    def __str__(self):
        return self.email