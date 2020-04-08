from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    last_request = models.DateTimeField(
        default=None,
        null=True,
    )

    def __str__(self):
        return f'User: {self.username}'
