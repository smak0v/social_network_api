from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=120,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
    )
    description = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    likes_count = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f'Post: {self.pk}'

    class Meta:
        ordering = [
            '-timestamp',
        ]


class PostLike(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'Post like: {self.pk}'

    class Meta:
        ordering = [
            '-timestamp',
        ]
