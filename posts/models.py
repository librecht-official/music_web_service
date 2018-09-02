from django.db import models
from people.models import User


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # SET_NULL ?
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)
