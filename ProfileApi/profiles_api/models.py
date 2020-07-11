from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for User Profiles"""

    def create_user(self, email, name, password=None):
        """Create a new User profile"""
        if not email:
            raise ValueError("Users must have an email Address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        #Set password encrypts the password field from plain text
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_super_user(self, email, name, password):
        """Creates a new Super User or Admin user"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user"""
        return str(self.name)

    def get_short_name(self):
        return self.name

    def __str__(self):
        """Returns String representation of the user"""
        return self.email

