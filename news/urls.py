from django.urls import path
from .views import *

urlpatterns = (
    path('inner/<int:id>/', inner, name='news.inner'),
)


