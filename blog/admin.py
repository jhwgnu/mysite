from django.contrib import admin
from blog.models import Post, Comment, Tag

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    def content_length(self, post):
        return '{}'.format(len(post.content))

    content_length.short_description = '글자수'

    list_display = ['id', 'title', 'content_length', 'created_at']
    list_display_links = ['title']
    list_filter = ['created_at']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
