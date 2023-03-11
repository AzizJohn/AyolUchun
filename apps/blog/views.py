from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.blog.models import PostCategory, Post, Interview
from apps.blog.serializers import (
    PostCategorySerializer, PostListSerializer, PostSerializer,
    InterviewListSerializer, InterviewSerializer,
)
from apps.common.tasks import update_view_count_task


# Create your views here.
###############################################################################
# ===========================  POST VIEWS  ====================================
###############################################################################
class PostCategoryListAPIView(ListAPIView):
    queryset = PostCategory.objects.all().oreder_by('name')
    serializer_class = PostCategorySerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all().oreder_by('-created_at')
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        update_view_count_task.delay(
            Post, instance, request.user, self.request.headers.get("device-id", None)
        )

        return Response(serializer.data)


###############################################################################
# ===========================  INTERVIEW VIEWS  ===============================
###############################################################################
class InterviewListAPIView(ListAPIView):
    queryset = Interview.objects.all().order_by('-created_at')
    serializer_class = InterviewListSerializer


class InterviewDetailAPIView(RetrieveAPIView):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
