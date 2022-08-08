from django.shortcuts import get_object_or_404
from rest_framework import permissions

from rest_framework import viewsets

from news.models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = PostSerializer

    permission_classes = [
        permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(News, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(News, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
