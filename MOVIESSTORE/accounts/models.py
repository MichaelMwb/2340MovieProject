from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
class CustomUser(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
=======
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)  # Birthdate field

    def __str__(self):
        return self.user.username
>>>>>>> 4b0cd93f860938d21c1efdb129804d2f57d8eeb3
