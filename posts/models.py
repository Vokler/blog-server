from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=64, blank=True)
    text = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
