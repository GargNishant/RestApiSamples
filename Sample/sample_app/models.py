from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserProfile(models.Model):
    firstName = models.CharField(max_length=30, blank=False)
    lastName = models.CharField(max_length=100, blank=False)
    address = models.TextField()
    mobile = models.IntegerField()
    email = models.CharField(max_length=200, blank=True, default="")
    isActive = models.BooleanField(default=True)
    password = models.CharField(max_length=200, blank=False, default="password")

    def __str__(self):
        return self.firstName


class Sessions(models.Model):
    # Work in Progress
    userId = models.IntegerField()
    session = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    deviceDetail = models.TextField()