from rest_framework import serializers
from .models import *


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ('name',)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'poster', 'author_id', 'view_count', 'full_text')
