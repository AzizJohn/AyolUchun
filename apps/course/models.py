from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from apps.dashboard.models import *
from apps.choices import *


class Category(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)
    icon = models.ImageField(upload_to="photos/category_icon%Y/%m/%d/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SocialMedia(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)
    icon = models.ImageField(upload_to="photos/socialmedia_icon%Y/%m/%d/")
    link = models.URLField()
    redirects = models.IntegerField()
    order = models.IntegerField()  # 1,2,3,4 for ordering social_medias

    def __str__(self):
        return self.name


class Interview(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    video_duration = models.TimeField()
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/interviews%Y/%m/%d/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"


class Course(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    badge_id = models.CharField(max_length=20, choices=BADGE_TYPE_CHOICES, blank=True,
                                null=True)  # static choice 1 for bestseller, 2 for tavsiya etiladi, 3 hech narsa
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    original_price = models.DecimalField(verbose_name=_('Price'), decimal_places=2, max_digits=10, default=0)
    discounted_price = models.DecimalField(verbose_name=_('Discount'), decimal_places=2, max_digits=10, default=0,
                                           null=True,
                                           blank=True)
    discount_expire_date = models.DateField()  # optional
    description = RichTextField(verbose_name=_("Description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class UserCourseConnection(BaseModel):
    course_id = models.ForeignKey(Course, verbose_name=_("Course"), on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    payment_state = models.CharField(max_length=30, choices=PAYMENT_STATUS_TYPE_CHOICES,
                                     default=BADGE_TYPE_CHOICES[1][0]
                                     )  # static choice 1: sotib olingan 2: sotib olinmagan 3: jarayonda

    def __str__(self):
        return self.course_id.title

    class Meta:
        verbose_name = "User Course Connection"
        verbose_name_plural = "User Course Connections"


class CourseComment(BaseModel):
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE)
    ranking = models.DecimalField(verbose_name=_('Ranking'), max_digits=5, decimal_places=2)
    comment_text = RichTextField(verbose_name=_('comment'))
    status = models.IntegerField(
        verbose_name=_('status'))  # optional 1: yoqqani ruxsat berilgani, 2: pending: kelib tushgani  3: yoqmagani

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        verbose_name = "Course Comment"
        verbose_name_plural = "Course Comments"


class Lecture(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'), blank=True, null=True)
    payment_state = models.IntegerField()  # static choice 1: sotib olmasdan ham ko'rish mumkin, 2: sotib olish majburiy
    order = models.IntegerField()  # for ordering lectures 1, 2, 3, 4, 5
    description = RichTextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"


class LectureComment(BaseModel):
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE)
    ranking = models.DecimalField(verbose_name=_('Ranking'), max_digits=5, decimal_places=2)
    comment_text = RichTextField(verbose_name=_('Comment'))
    status = models.IntegerField()  # 1: active yoqqani, 2: pending= kelib tushgani  3: deleted=yoqmagani
    reply_lecture_comment_id = models.ForeignKey('self', verbose_name=_('Reply to Comment'), null=True, blank=True,
                                                 on_delete=models.CASCADE,
                                                 related_name='replies')

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        verbose_name = "Lecture Comment"
        verbose_name_plural = "Lecture Comments"


class Video(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'), blank=True, null=True)
    duration_time = models.TimeField(verbose_name=_('Video Duration'))
    order = models.IntegerField()  # for ordering videos 1, 2, 3, 4, 5
    lecture_id = models.ForeignKey(Lecture, verbose_name=_('Lecture'), on_delete=models.CASCADE)
    required_video_id = models.ForeignKey('self', verbose_name=_('Required Video'), on_delete=models.CASCADE,
                                          blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class UserVideoViewedRelation(BaseModel):
    video_id = models.ForeignKey(Video, verbose_name=_('Video'), on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)

    def __str__(self):
        return self.video_id.title

    class Meta:
        verbose_name = "User Viewed Video"
        verbose_name_plural = "User Viewed Videos"


class Certificate(BaseModel):
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE)
    certificate_photo = models.ImageField(upload_to="photos/certificate%Y/%m/%d/")

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
