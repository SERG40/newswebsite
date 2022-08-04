from django.contrib import admin
from django.urls import path

from news.views import index, create_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create_news, name='create_news'),
]
