from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserProfile(models.Model):
    firstName = models.CharField(max_length=30, blank=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    address = models.TextField()
    mobile = models.IntegerField(unique=True)
    email = models.CharField(max_length=200, blank=False, unique=True)
    isActive = models.BooleanField(default=True)
    password = models.CharField(max_length=200, blank=False,null=False)

    def __str__(self):
        return self.firstName


class Sessions(models.Model):
    # Work in Progress
    user = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE)
    session = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    deviceDetail = models.TextField(default="NA", blank=True)
