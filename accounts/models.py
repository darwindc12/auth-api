from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
        ('service', 'Service'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin'
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"