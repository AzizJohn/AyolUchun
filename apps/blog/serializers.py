from rest_framework import serializers
from apps.blog.models import PostCategory, Post, Interview


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'image', 'author', 'view_count', 'full_text')
