from django.contrib.auth.models import User
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title