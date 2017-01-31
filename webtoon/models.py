from django.db import models

class Webtoon(models.Model):
        title = models.CharField(max_length=100, verbose_name = '제목', help_text = '제목을 입력하세요')
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.title
