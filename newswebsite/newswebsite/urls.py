from django.contrib import admin
from django.urls import path
from news import views
from news.views import index, create_news, post_detail, add_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('create/', create_news, name='create_news'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:id>/', views.edit, name='post_edit'),
    path('delete/<int:id>/', views.delete),
    path('<int:id>/comment/', add_comment, name='add_comment'),
]
