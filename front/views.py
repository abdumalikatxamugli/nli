from django.http import HttpResponse
from django.shortcuts import render
from front.models import News


def news(request):
    context = {
        'news': News.objects.all()
    }
    return render(request, 'index.html', context)

def news_inner(request,pk):
    context = {
        'text' : News.objects.get(id=pk)
    }
    return render(request, 'inner.html', context)