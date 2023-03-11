from rest_framework import serializers

from apps.blog.models import PostCategory, Post, Interview
from apps.common.serializers import AuthorSerializer


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ('id', 'name')


class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'image', 'author', 'view_count', 'created_at',
        )


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'image', 'author', 'view_count',
            'content', 'created_at', 'modified_at',
        )


class InterviewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Interview
        fields = (
            'id', 'title', 'image', 'video', 'author', 'text',
            'created_at', 'modified_at',
        )
