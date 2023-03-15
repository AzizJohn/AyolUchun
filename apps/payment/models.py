from django.db import models
from django.utils.translation import gettext as _

from apps.course.models import Course
from apps.users.models import User
from apps.common.models import BaseModel
from apps.common.choices import PAYMENT_TYPE_CHOICES, PAYMENT_STATUS_CHOICES


class Payment(BaseModel):
    course = models.ForeignKey(
        Course, verbose_name=_('Course'), on_delete=models.CASCADE, related_name='course_payments'
    )
    payer = models.ForeignKey(
        User, verbose_name=_('Payer'), on_delete=models.CASCADE, related_name='course_payments'
    )
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)
    payment_type = models.CharField(
        max_length=20, verbose_name=_('Payment_type'), choices=PAYMENT_TYPE_CHOICES,
        blank=True, null=True
    )
    payed_at = models.DateTimeField(
        verbose_name=_('Payment date'), blank=True, null=True
    )  # to'langan sana vaqti; :: created_at-- to'lov knopkasi bosilgandagi vaqt
    payment_status = models.CharField(
        max_length=20, verbose_name=_('Payment Status'),
        choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_CHOICES[0][0]
    )

    def __str__(self):
        return f"{self.course.title} {self.price}"
