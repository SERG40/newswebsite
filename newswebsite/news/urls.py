from django.urls import path
from news import views
from .views import index, create_news, post_detail, add_comment, DeleteComment, AddLike, AddDislike

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_news, name='create_news'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:id>/', views.edit, name='post_edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('<int:id>/comment/', add_comment, name='add_comment'),
    path('dele/<int:id>/', DeleteComment, name='del'),
    path('<int:pk>/like/', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike/', AddDislike.as_view(), name='dislike')
]