from django.urls import path

from apps.blog.api.views import (
    PostCategoryListAPIView,
    PostCategoryDetailAPIView,
    PostListAPIView,
    PostDetailAPIView,
    InterviewListAPIView,
    InterviewDetailAPIView,
)


app_name = 'blog'

urlpatterns = [
    # category urls
    path('categories/list/', PostCategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/detail/', PostCategoryDetailAPIView.as_view(), name='category-detail'),
    # post urls
    path('posts/list/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/detail/', PostDetailAPIView.as_view(), name='post-detail'),
    # interview urls
    path('interviews/list/', InterviewListAPIView.as_view(), name='interview-list'),
    path('interviews/<int:pk/detail/', InterviewDetailAPIView.as_view(), name='interview-detail'),

]
