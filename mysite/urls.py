from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views
from webtoon import views as webtoon_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.post_list),
    url(r'^(?P<pk>\d+)/$', blog_views.post_detail),
    url(r'^webtoon/$', webtoon_views.webtoon_list),
    url(r'^webtoon/(?P<id>\d+)$', webtoon_views.webtoon_detail),
]
