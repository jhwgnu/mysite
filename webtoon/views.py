from django.shortcuts import render
from .models import Webtoon


def webtoon_list(request):
    return render(request, 'webtoon/webtoon_list.html', {
        'webtoon_list':Webtoon.objects.all(),
    })


def webtoon_detail(request, id):
    webtoon = Webtoon.objects.get(id=id)
    return render(request, 'webtoon/webtoon_detail.html', {
        'webtoon': webtoon,
    })
