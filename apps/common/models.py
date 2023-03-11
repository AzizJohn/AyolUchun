from django.db import models
from django.utils.translation import gettext as _
from apps.choices import GENDER_TYPE_CHOICES


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    class Meta:
        abstract = True


class Author(BaseModel):
    profile_pic = models.ImageField(upload_to="photos/avatar/%Y/%m/%d/", blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE_CHOICES)
    first_name = models.CharField(max_length=50, verbose_name=_("Name"))
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
