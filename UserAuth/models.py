from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name}"
