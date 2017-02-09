from django.shortcuts import render
from news.models import Article

def article_list(request):
    return render(request, 'news/article_list.html', {
        'articles': Article.objects.all(),
    })

def article_detail(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, 'news/article_detail.html', {
        'article': article,
    })
