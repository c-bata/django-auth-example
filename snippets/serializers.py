from rest_framework import serializers

from .models import Snippet, Comment


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'code', 'description', 'created_by', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text', 'commented_at', 'commented_to', 'commented_by')
