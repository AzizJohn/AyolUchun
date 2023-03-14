import datetime
import random
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

from apps.users.services.generators import random_phone_generator, random_username_generator, random_code_generator
from apps.common.choices import GENDER_TYPE_CHOICES, AUTH_STATUS
from apps.common.models import BaseModel


class Position(BaseModel):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class CustomUserManager(UserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone_number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, password, **extra_fields)


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
    phone_number = PhoneNumberField(
        verbose_name=_('Phone Number'),
        unique=True,
        error_messages={
            "unique": _("A user with that phone number already exists."),
        }
    )
    is_email_confirmed = models.BooleanField(default=False)

    # socials
    instagram_account = models.CharField(max_length=30, verbose_name=_('Instagram'), blank=True, null=True)
    imkon_account = models.CharField(max_length=30, verbose_name=_('Imkon'), blank=True, null=True)
    linkedin_account = models.CharField(max_length=30, verbose_name=_('Linkedin'), blank=True, null=True)

    # about
    work_place = models.CharField(max_length=100, verbose_name=_('Work Place'), blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(verbose_name=_('Biography'), null=True, blank=True)

    auth_status = models.CharField(max_length=20, choices=AUTH_STATUS, default=AUTH_STATUS[0][0])

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    @property
    def age(self):
        if self.birthdate is not None:
            current_date = timezone.now().date()
            duration = current_date - self.birthdate
            return duration.days // 365

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def create_phone_verify_code(self):
        code = random_code_generator()
        UserCodeConfirmation.objects.create(
            user_id=self.id,
            code=code
        )
        return code

    def check_phone_number(self):
        if not self.phone_number:
            temp_phone = random_phone_generator()
            while User.objects.filter(phone_number=temp_phone).exists():
                temp_phone = random_phone_generator()
            self.phone_number = temp_phone

    def check_username(self):
        if not self.username:
            temp_username = random_username_generator(self.first_name)
            while User.objects.filter(username=temp_username).exists():
                temp_username = random_username_generator(temp_username)
            self.username = temp_username

    def check_pass(self):
        if not self.password:
            temp_password = "password12345"
            self.password = temp_password

    def save(self, *args, **kwargs):
        self.check_phone_number()
        self.check_username()
        self.check_pass()
        super().save(*args, **kwargs)

    def get_token(self):
        token, created = Token.objects.get_or_create(user=self)

        return {'token': token.key}

    def __str__(self):
        return f"{str(self.id)} | {str(self.phone_number)}"


class UserCodeConfirmation(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='confirmation_codes'
    )
    code = models.CharField(max_length=6)
    is_confirmed = models.BooleanField(default=False)
    expired_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.id is None:
            # if user is being created, set expired_at field with 3 minutes duration
            self.expired_at = timezone.now() + datetime.timedelta(minutes=3)
        super().save(*args, **kwargs)

    def set_is_confirmed_true(self):
        self.is_confirmed = True
        self.save()

    def __str__(self):
        return f"{self.user} | {self.code}"
