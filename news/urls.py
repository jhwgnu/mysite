from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^(?P<pk>\d+)$', views.article_detail, name='article_detail'),
]
