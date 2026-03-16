from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('technician', 'Technician'),
        ('department_user', 'Department User'),
        ('inventory_manager', 'Inventory Manager'),
        ('auditor', 'Auditor'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin'
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"