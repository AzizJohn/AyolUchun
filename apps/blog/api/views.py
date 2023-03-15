from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models import PostCategory, Post, Interview
from apps.blog.api.serializers import (
    PostCategorySerializer, PostListSerializer, PostSerializer,
    InterviewListSerializer, InterviewSerializer,
)
from apps.blog.services.tasks import update_post_view_task
from apps.common.paginations import CustomPagination


# Create your views here.
###############################################################################
# ===========================  POST VIEWS  ====================================
###############################################################################
class PostCategoryListAPIView(ListAPIView):
    queryset = PostCategory.objects.all().order_by('name')
    serializer_class = PostCategorySerializer


class PostCategoryDetailAPIView(RetrieveAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer

    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('category', )
    search_fields = ('title', 'author__first_name', 'author__last_name', )


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        update_post_view_task.delay(
            instance.id, request.user.id, self.request.headers.get("device-id", None)
        )

        return Response(serializer.data)


###############################################################################
# ===========================  INTERVIEW VIEWS  ===============================
###############################################################################
class InterviewListAPIView(ListAPIView):
    queryset = Interview.objects.all().order_by('-created_at')
    serializer_class = InterviewListSerializer

    pagination_class = CustomPagination


class InterviewDetailAPIView(RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
