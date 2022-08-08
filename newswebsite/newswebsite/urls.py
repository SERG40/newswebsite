from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('news.urls')),
    path('', include('users.urls')),
    path('', include('django.contrib.auth.urls')),
]
