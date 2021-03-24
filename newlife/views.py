from django.shortcuts import render
from django.template import loader
from news.models import News

def index(request):
    news = News.objects.all()[:3]
    context = {
        'news': news
    }
    return render(request, 'index.html', context)