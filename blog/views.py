from django.shortcuts import render
from blog.models import Post, Comment
# from django.http import HttpResponse

def post_list(request):
    # return HttpResponse("리스트 만들기")
    return render(request, 'blog/post_list.html', {
        'post_list': Post.objects.all(),
    })

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })
