from rest_framework.serializers import ModelSerializer

from apps.common.serializers import AuthorSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'icon')


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('id', 'name', 'icon', 'link', 'redirects', 'order')


class CourseSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category_id = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'badge_id', 'author', 'category_id', 'original_price', 'discounted_price',
            'discount_expire_date',
            'description')


class CourseCommentSerializer(ModelSerializer):
    user_id = UserSerializer(read_only=True)
    course_id = CourseSerializer(read_only=True)

    class Meta:
        model = CourseComment
        fields = ('id', 'user_id', 'course_id', 'ranking', 'comment_text', 'status')


class SectionSerializer(ModelSerializer):
    course_id = CourseSerializer(read_only=True)

    class Meta:
        model = Section
        fields = ('id', 'course_id', 'title', 'index')


class LectureSerializer(ModelSerializer):
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'title', 'is_paid', 'order', 'video', 'section', 'description')


class LectureViewed(ModelSerializer):
    lecture = LectureSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        fields = ('id', 'lecture', 'user')


class LectureCommentSerializer(ModelSerializer):
    user_id = UserSerializer(read_only=True)
    lecture = LectureSerializer(read_only=True)

    # replies = 'self'

    class Meta:
        model = LectureComment
        fields = ('id', 'user_id', 'lecture', 'comment_text', 'status', 'replies', 'index')


class CertificateSerializer(ModelSerializer):
    user_id = UserSerializer(read_only=True)
    course_id = CourseSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'user_id', 'course_id', 'certificate_photo')
