from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('journal:post_detail', args=[self.pk])

    def __str__(self):
        return self.title
