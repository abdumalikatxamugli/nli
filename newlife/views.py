from django.shortcuts import render
from django.template import loader
from news.models import News
from sales.models import Product


def index(request):
    news = News.objects.all()[:3]
    products = Product.objects.all()
    context = {
        'news': news,
        'products': products
    }
    return render(request, 'index.html', context)