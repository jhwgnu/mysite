from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name = '제목', help_text = '제목을 입력하세요')
    content = models.TextField(verbose_name = '내용', help_text = '내용을 입력하세요')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
