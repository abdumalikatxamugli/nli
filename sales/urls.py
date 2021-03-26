from django.conf import settings
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from .views import *

urlpatterns = [
    path('form/<int:product_id>/', get_product_form, name='sales.form'),
    path('product/<int:id>/', get_product, name='sales.index'),
    path('login', login, name='sales.login'),
    path('logout', logout, name='sales.logout')
]