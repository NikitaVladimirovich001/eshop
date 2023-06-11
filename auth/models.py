from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        if not email or not email:
            raise ValueError('Email или password является None!')
        if 'username' not in kwargs.keys():
            raise ValueError('Username должен быть задан!')


        user = CustomUser(email=email, **kwargs)
        user.is_active = user.is_superuser
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, *args, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True

        return self.create_user(email, password, *args, **kwargs)


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=128,
                              unique=True,
                              db_index=True,
                              blank=False)
    is_active = models.BooleanField(blank=False,
                                    default=False)
    # last_entry_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    object = CustomUserManager()