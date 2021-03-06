"""newlife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from .views import index

admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'New Life Insurance'

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path('', index, name="home"),
    path('about/', include('aboutus.urls')),
    path('news/', include('news.urls'))
)



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
