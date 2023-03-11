from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel, Author
from apps.course.models import *
from apps.payment.models import *
from apps.dashboard.models import *
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField


class PostCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"


class Post(BaseModel):
    poster = models.ImageField(upload_to="photos/post_image%Y/%m/%d/", verbose_name=_('photo'), blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Title', blank=True, null=True)
    author = models.ForeignKey(Author, verbose_name=_('Author'), on_delete=models.CASCADE)
    view_count = models.IntegerField()
    full_text = RichTextField(verbose_name=_('Post Content'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Interview(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to="videos/interview_video/%Y/%m/%d/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/interviews/%Y/%m/%d/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"
