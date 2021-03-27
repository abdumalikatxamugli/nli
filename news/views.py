from django.shortcuts import render
from news.models import *

def inner(request, id):
    news = News.objects.get(pk=id)
    context = {
        'news': news
    }
    return render(request, 'news/inner.html', context)