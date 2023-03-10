from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from apps.course.models import *
from apps.dashboard.models import *


class Advertisement(BaseModel):
    full_text = RichTextField(verbose_name=_('Text'), blan=True, null=True)
    phone = PhoneNumberField(verbose_name=_('Phone number'), blank=True, null=True)

    def __str__(self):
        return f"Adds"

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


class Feedback(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Name'), blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True)
    phone = PhoneNumberField(verbose_name=_('Phone'), blank=True, null=True)
    message = RichTextField(verbose_name=_('Feedback message'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class Notification(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'), blank=True, null=True)
    context = RichTextField(verbose_name=_('Context'), blank=True, null=True)
    is_viewed = models.BooleanField(
        default=False, help_text="checking the status of notification T --> viewed")  # for checking the status of notification is viewed or not: True --> viewed, False --> not viewed
    user_id = models.ForeignKey(User, verbose_name=_('User'), on_delete=models.SET_NULL, blank=True,
                                null=True)  # for which user we sent a notification
    scheduled_time = models.DateTimeField(verbose_name=_('schedule'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
