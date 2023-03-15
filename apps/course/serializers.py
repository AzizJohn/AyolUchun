from django.db.models import Avg, Count
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ..common.serializers import AuthorSerializer
from ..course.models import Category, Course, CourseComment, CourseUser, SocialMedia, Section, Lecture, LectureComment, \
    Certificate, LectureViewed
from ..users.models import User


class CourseUserSerializer(ModelSerializer):
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
    #purchased_users=SerializerMethodField()
    four_enrolled_users = SerializerMethodField()
    is_purchased = SerializerMethodField()
    average_rating = SerializerMethodField()

    def get_is_purchased(self, course):
        return CourseUser.objects.filter(
            course=course.id, user=self.context['request'].user.id).exists()

    def get_four_enrolled_users(self, course):
        course_users = CourseUser.objects.filter(
            course_id=course.id).order_by('-created_at')[:4]
        users = []

        for course_user in course_users:
            users.append(course_user.user)

        ser = CourseUserSerializer(users, many=True).data

        return ser

    def get_average_rating(self, obj):
        course_rating = CourseComment.objects.aggregate(Avg('ranking'))['ranking__avg']
        return course_rating

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'badge_id', 'author', 'category_id', 'original_price', 'discounted_price',
            'discount_expire_date', 'four_enrolled_users',
            'description', 'is_purchased', 'average_rating')


class CourseCommentSerializer(ModelSerializer):
    user_id = CourseUserSerializer(read_only=True)
    course_id = CourseSerializer(read_only=True)

    def get_course_comments(self, course):
        course_comments = CourseComment.objects.filter(
            course_id=course.id).order_by('-created_at')
        comments = []

        for course_comment in course_comments:
            comments.append(course_comment)

        ser = CourseCommentSerializer(comments, many=True).data

        return ser

    class Meta:
        model = CourseComment
        fields = ('id', 'user_id', 'course_id', 'ranking', 'comment_text', 'status')


class SectionSerializer(ModelSerializer):
    course_id = CourseSerializer(read_only=True)
    section_status = SerializerMethodField()

    # lecture_number = SerializerMethodField()

    # def get_lecture_number(self, section_id):
    #     lecture_number = Lecture.objects.filter(sectionid=section_id).count()
    #     return lecture_number

    def get_section_status(self, section):

        # return section.section_lectures.all().count() == LectureViewed.objects.filter(lecture__section=section, user=self.context['request'].user.id).count()
        print()
        if Lecture.is_paid == 1:
            if section.course_id.course_payments.all().filter(payer_id=self.context['request'].user.id).count() == 1:
                viewed_lecture_count = Lecture.objects.filter(section_id=section).annotate(
                    view_count=Count('lecture_viewed')).values('view_count').aggregate(total_views=Count('view_count'))
                if viewed_lecture_count['total_views'] == 0:
                    return 'Not Started'
                elif viewed_lecture_count['total_views'] < Lecture.objects.filter(section=section).count():
                    return 'In Progress'
                else:
                    return 'Completed'
            else:
                return 'Not Purchased'
        else:
            viewed_lecture_count = Lecture.objects.filter(section=section).annotate(
                view_count=Count('lecture_viewed')).values('view_count').aggregate(total_views=Count('view_count'))
            if viewed_lecture_count['total_views'] == 0:
                return 'Not Started'
            elif viewed_lecture_count['total_views'] < Lecture.objects.filter(section=section).count():
                return 'In Progress'
            else:
                return 'Completed'

    class Meta:
        model = Section
        fields = ('id', 'course_id', 'title', 'index', 'section_status')


class LectureSerializer(ModelSerializer):
    section = SectionSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ('id', 'title', 'is_paid', 'order', 'video', 'section', 'description')


class LectureViewedSerializer(ModelSerializer):
    lecture = LectureSerializer(read_only=True)
    user = CourseUserSerializer(read_only=True)

    class Meta:
        model = LectureViewed
        fields = ('id', 'lecture', 'user')


class LectureCommentSerializer(ModelSerializer):
    user_id = CourseUserSerializer(read_only=True)
    lecture = LectureSerializer(read_only=True)
    replies = SerializerMethodField()

    class Meta:
        model = LectureComment
        fields = ('id', 'user_id', 'lecture', 'comment_text', 'status', 'replies', 'index')

    def get_replies(self, obj):
        if obj.replies.count() == 0:
            return None
        serializer = self.__class__(obj.replies.all(), many=True)
        return serializer.data


class CertificateSerializer(ModelSerializer):
    user_id = CourseUserSerializer(read_only=True)
    course_id = CourseSerializer(read_only=True)

    class Meta:
        model = Certificate
        fields = ('id', 'user_id', 'course_id', 'certificate_photo')
