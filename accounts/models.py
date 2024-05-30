from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Add any additional fields if needed
    # For example: additional_field = models.CharField(max_length=100, blank=True, null=True)
    custom_role = models.CharField(max_length=100, blank=True, null=True)