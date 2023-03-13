from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _

from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField
from apps.common.choices import GENDER_TYPE_CHOICES
from apps.common.models import BaseModel


class Position(BaseModel):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    # general
    avatar = ImageField(upload_to="photos/avatars/%Y/%m/%d/", verbose_name=_('Avatar'))
    birthdate = models.DateField(verbose_name=_('Birthdate'), blank=True, null=True)
    gender = models.CharField(
        max_length=10, verbose_name=_('Gender'), choices=GENDER_TYPE_CHOICES,  # choices  (male and female)
        blank=True, null=True
    )

    # for contact
    country = models.CharField(max_length=50, verbose_name=_('Country'), blank=True, null=True)
    region = models.CharField(max_length=50, verbose_name=_('Region'), blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=_('Address'), blank=True, null=True)
    postal_index = models.CharField(max_length=20, verbose_name=_('Postal Index'), blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_('Phone Number'))
    is_email_confirmed = models.BooleanField(default=False)

    # socials
    instagram_account = models.CharField(max_length=30, verbose_name=_('Instagram'), blank=True, null=True)
    imkon_account = models.CharField(max_length=30, verbose_name=_('Imkon'), blank=True, null=True)
    linkedin_account = models.CharField(max_length=30, verbose_name=_('Linkedin'), blank=True, null=True)

    # about
    work_place = models.CharField(max_length=100, verbose_name=_('Work Place'), blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(verbose_name=_('Biography'), null=True, blank=True)

    @property
    def age(self):
        if self.birthdate is not None:
            current_date = timezone.now().date()
            duration = current_date - self.birthdate
            return duration.days // 365

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
