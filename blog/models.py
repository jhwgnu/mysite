from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now=True)
