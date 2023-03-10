from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from apps.choices import *


class User(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name=_('Name'), blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name=_('Surname'), blank=True, null=True)
    avatar = models.ImageField(upload_to="photos/avatars%Y/%m/%d/", verbose_name=_('Avatar'))
    username = models.CharField(max_length=50, verbose_name=_('Username'), blank=True, null=True)
    password = models.CharField(max_length=100, verbose_name=_('Password'), blank=True, null=True)
    role_id = models.IntegerField(verbose_name=_("Role"))  # 1: ordinary user,  2: admin ...
    profession = models.CharField(max_length=50, verbose_name=_('Profession'), blank=True,
                                  null=True)  # Tilshunos lavozimi
    country = models.CharField(max_length=50, verbose_name=_('Country'), blank=True, null=True)
    region = models.CharField(max_length=50, verbose_name=_('Region'), blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=_('Address'), blank=True, null=True)
    postal_index = models.CharField(max_length=20, verbose_name=_('Postal Index'), blank=True, null=True)
    phone = PhoneNumberField(verbose_name=_('Phone Number'))
    instagram_account = models.CharField(max_length=30, verbose_name=_('Instagram'), blank=True, null=True)
    imkon_account = models.CharField(max_length=30, verbose_name=_('Imkon'), blank=True, null=True)
    linkedin_account = models.CharField(max_length=30, verbose_name=_('Linkedin'), blank=True, null=True)
    work_place = models.CharField(max_length=100, verbose_name=_('Work Place'), blank=True, null=True)
    bio = RichTextField(verbose_name=_('Biography'))
    birthdate = models.DateField(verbose_name=_('Birthdate'))  # age ni shu ma'lumot bilan hisoblab olsa bo'ladi
    email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True)
    email_confirmation_link = models.URLField(verbose_name=_('Confirmation Link'))
    email_confirmation_status = models.IntegerField(
        help_text="confirmation status enter 1, 2 or 3")  # 1: confirmed, 2:unconformed, 3: confirmtion_iloji yo'q
    gender = models.CharField(max_length=10, verbose_name=_('Gender'), choices=GENDER_TYPE_CHOICES, blank=True,
                              null=True)  # choice  (male and female)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
