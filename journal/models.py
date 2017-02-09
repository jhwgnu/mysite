from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DataTimeField(auto_now_add=True)
    created_at = models.DataTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('journal:post_detail', args=[self.pk])
