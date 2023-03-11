from rest_framework.generics import ListAPIView

from apps.blog.models import PostCategory
from apps.blog.serializers import PostCategorySerializer


# Create your views here.
class PostCategoryListAPIView(ListAPIView):
    queryset = PostCategory.objects.all().oreder_by('name')
    serializer_class = PostCategorySerializer




