from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField

from apps.choices import *
from apps.common.models import Author
from apps.common.models import BaseModel
from apps.dashboard.models import User


class Category(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)
    icon = ImageField(upload_to="photos/category_icon/%Y/%m/%d/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SocialMedia(BaseModel):
    name = models.CharField(max_length=30, blank=True, null=True)
    icon = ImageField(upload_to="photos/socialmedia_icon/%Y/%m/%d/")
    link = models.URLField()
    redirects = models.IntegerField()
    order = models.IntegerField()  # 1,2,3,4 for ordering social_medias

    def __str__(self):
        return self.name


class Course(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    badge_id = models.CharField(max_length=20, choices=BADGE_TYPE_CHOICES, blank=True,
                                null=True)  # static choice 1 for bestseller, 2 for tavsiya etiladi, 3 hech narsa
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
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


class Section(BaseModel):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    index = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"


class Lecture(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_('title'), blank=True, null=True)
    is_paid = models.BooleanField()
    order = models.IntegerField()  # for ordering lectures 1, 2, 3, 4, 5
    video = models.FileField(upload_to="videos/lecture_video/%Y/%m/%d/")
    description = RichTextField(verbose_name=_('Description'))
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lecture"
        verbose_name_plural = "Lectures"


class LectureViewed(BaseModel):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class LectureComment(BaseModel):
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, verbose_name=_('Lecture'), on_delete=models.CASCADE)

    comment_text = models.TextField(verbose_name=_('Comment'))
    status = models.IntegerField()  # 1: active yoqqani, 2: pending= kelib tushgani  3: deleted=yoqmagani
    reply_lecture_comment_id = models.ForeignKey('self', verbose_name=_('Reply to Comment'), null=True, blank=True,
                                                 on_delete=models.CASCADE,
                                                 related_name='replies')
    index = models.IntegerField()

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        verbose_name = "Lecture Comment"
        verbose_name_plural = "Lecture Comments"


class Certificate(BaseModel):
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE)
    certificate_photo = ImageField(upload_to="photos/certificate/%Y/%m/%d/")

    def __str__(self):
        return self.user_id.first_name

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"
