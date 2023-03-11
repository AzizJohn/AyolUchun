from rest_framework.serializers import ModelSerializer

from apps.common.models import Author
from .models import *


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('Profile_pic', 'gender', 'first_name', 'last_name', 'email', 'bio')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'icon')


class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('name', 'icon', 'link', 'redirects', 'order')


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'title', 'badge_id', 'author', 'category_id', 'original_price', 'discounted_price', 'discount_expire_date',
            'description')


class CourseCommentSerializer(ModelSerializer):
    class Meta:
        model = CourseComment
        fields = ('user_id', 'course_id', 'ranking', 'comment_text', 'status')


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ('course_id', 'title', 'index')


class LectureSerializer(ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('title', 'is_paid', 'order', 'video', 'section', 'description')


class LectureViewed(ModelSerializer):
    class Meta:
        fields = ('lecture', 'user')


class LectureCommentSerializer(ModelSerializer):
    class Meta:
        model = LectureComment
        fields = ('user_id', 'lecture', 'comment_text', 'status', 'reply_lecture_comment_id', 'index')


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('user_id', 'course_id', 'certificate_photo')
