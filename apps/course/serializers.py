from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'icon')


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('name', 'icon', 'link', 'redirects', 'order')


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ('title', 'video_duration', 'creator_id', 'photo')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title', 'badge_id', 'author', 'category_id', 'original_price', 'discounted_price', 'discount_expire_date',
            'description')


class UserCourseConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCourseConnection
        fields = ('course_id', 'user_id', 'payment_state')


class CourseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseComment
        fields = ('user_id', 'course_id', 'ranking', 'comment_text', 'status')


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('title', 'payment_state', 'order', 'description')


class LectureCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureComment
        fields = ('user_id', 'course_id', 'ranking', 'comment_text', 'status', 'reply_lecture_comment_id')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'duration_time', 'order', 'lecture_id', 'required_video_id')


class UserVideoViewedRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVideoViewedRelation
        fields = ('video_id', 'user_id')


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('user_id', 'course_id', 'certificate_photo')
       