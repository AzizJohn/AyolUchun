from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.blog.models import PostCategory, Post
from apps.blog.serializers import PostCategorySerializer, PostListSerializer, PostSerializer


# Create your views here.
class PostCategoryListAPIView(ListAPIView):
    queryset = PostCategory.objects.all().oreder_by('name')
    serializer_class = PostCategorySerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().oreder_by('-created_at')
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





