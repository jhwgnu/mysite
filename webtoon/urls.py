from django.conf.urls import url
from webtoon import views

urlpatterns = [
    url(r'^webtoon/$', views.webtoon_list),
    url(r'^webtoon/(?P<id>\d+)$', views.webtoon_detail),
]
