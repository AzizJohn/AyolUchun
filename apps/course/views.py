from rest_framework import generics

from . import serializers
from .models import *
from .permissions import IsAdminOrCreateOnly


class CategoryList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class SocialMediaList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer


class CourseList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class CourseCommentList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = CourseComment.objects.all()
    serializer_class = serializers.CourseCommentSerializer


class SectionList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Section.objects.all()
    serializer_class = serializers.SectionSerializer


class LectureList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Lecture.objects.all()
    serializer_class = serializers.LectureSerializer


class LectureViewedList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = LectureViewed.objects.all()
    serializer_class = serializers.LectureViewed


class LectureCommentList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = LectureComment.objects.all()
    serializer_class = serializers.LectureCommentSerializer


class CertificateList(generics.ListAPIView):
    permission_classes = (IsAdminOrCreateOnly,)
    queryset = Certificate.objects.all()
    serializer_class = serializers.CertificateSerializer
