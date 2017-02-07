from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect
# from blog import views as blog_views
# from webtoon import views as webtoon_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda request: redirect('blog:post_list')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^webtoon/', include('webtoon.urls', namespace='webtoon')),
    url(r'^journal/', include('journal.urls', namespace='journal')),
]
