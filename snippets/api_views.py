from rest_framework import viewsets, filters

from .models import Snippet, Comment
from .serializers import SnippetSerializer, CommentSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'created_at',)
    ordering = ('created_at',)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('commented_at',)
    ordering = ('commented_at',)
