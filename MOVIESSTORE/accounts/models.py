from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
