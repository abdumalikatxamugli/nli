from django.urls import path
from .views import *

urlpatterns = [
    path('', general, name='aboutus.index'),
    path('license/', license, name='aboutus.license'),
    path('management/', management, name='aboutus.management'),
    path('reports/', reports, name='aboutus.reports')
]
