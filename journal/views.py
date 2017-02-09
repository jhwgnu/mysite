from django.shortcuts import render
from journal.models import Post
# from django.http import HttpResponse

def post_list(request):
    return render(request, 'journal/post_list.html', {
        'post_list': Post.objects.all(),
    })
#
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'journal/post_detail.html', {
        'post': post,
    })
#
# def post_new(request):
#     print(request.GET)
#     print(request.POST)
#     print(request.FILES)
#     return render(request, 'blog/post_form.html')
