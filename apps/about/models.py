from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField

from apps.common.models import BaseModel
from apps.users.models import User


class Feedback(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), blank=True, null=True)
    message = RichTextField(verbose_name=_('Feedback message'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class Notification(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'), blank=True, null=True)
    context = RichTextField(verbose_name=_('Context'), blank=True, null=True)
    scheduled_at = models.DateTimeField(verbose_name=_('schedule time'), default=timezone.now)

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-created_at']

    @classmethod
    def get_unread_notifications(cls, user):
        now = timezone.now()
        queryset = cls.objects.filter(
            scheduled_at__lte=now, created_at__gte=user.created_at
        ).execute(notification_views__user=user)

        return queryset

    def __str__(self):
        return self.title


class NotificationView(BaseModel):
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE,
        related_name='notification_views'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.notification.title[:20]}... | {self.user}"


class Advertisement(BaseModel):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = ImageField(upload_to="photos/advertisement/%Y/%m/%d/")
    content = RichTextField(verbose_name=_('Content'))
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        return "Advertisement"


class UseTerm(BaseModel):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = ImageField(upload_to="photos/notification_images/%Y/%m/%d/")
    content = RichTextField(verbose_name=_('Content'))

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        return "UseTerm"


class Contact(BaseModel):
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    email = models.EmailField()
    address = models.CharField(max_length=150)
    long = models.FloatField()
    lat = models.FloatField()

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"

    def __str__(self):
        return "UseTerm"
