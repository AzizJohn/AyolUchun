from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _
from sorl.thumbnail import ImageField

from apps.common.models import BaseModel, Author


class PostCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Post Category"
        verbose_name_plural = "Post Categories"
        ordering = ['name']


class Post(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Title')
    category = models.ForeignKey(
        PostCategory, on_delete=models.CASCADE, related_name='posts'
    )
    image = models.ImageField(upload_to="photos/post_images/%Y/%m/%d/", verbose_name=_('photo'))
    author = models.ForeignKey(
        Author, verbose_name=_('Author'), on_delete=models.CASCADE,
        related_name='posts'
    )
    view_count = models.IntegerField(default=0)
    content = RichTextUploadingField(verbose_name=_('Post Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class PostView(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post_views'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_views',
        null=True, blank=True
    )
    device_id = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.post.title[:20]}... | {self.user} | {self.device_id}"


class Interview(BaseModel):
    title = models.CharField(max_length=255)
    image = ImageField(upload_to='photos/interviews/%Y/%m/%d/')
    video = models.FileField(upload_to='videos/interviews/%Y/%m/%d/')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='interviews'
    )
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Interview"
        verbose_name_plural = "Interviews"

