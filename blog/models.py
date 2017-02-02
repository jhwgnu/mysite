from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name = '제목', help_text = '제목을 입력하세요')
    content = models.TextField(verbose_name = '내용', help_text = '내용을 입력하세요')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
