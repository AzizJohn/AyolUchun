from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel
from apps.course.models import *
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from apps.choices import *


class Payment(BaseModel):
    course_id = models.ForeignKey(Course, verbose_name=_('Course'), on_delete=models.CASCADE)
    payer_user_id = models.ForeignKey(User, verbose_name=_('Payer'), on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=5, decimal_places=2)
    payment_type_id = models.CharField(max_length=20, verbose_name=_('Payment_type'), choices=PAYMENT_TYPE_CHOICES,
                                       blank=True, null=True)  # static choice 1: Visa, 2: click
    payed_at = models.DateTimeField(verbose_name=_('Payment date'), blank=True,
                                    null=True)  # to'langan sana vaqti; :: created_at-- to'lov knopkasi bosilgandagi vaqt
    payment_status = models.CharField(max_length=20, verbose_name=_('Payment Status'),
                                      choices=PAYMENT_STATUS_TYPE_CHOICES, default=PAYMENT_STATUS_TYPE_CHOICES[1][0])  # 1: to'lanmagan 2: to'langan 3: o'chirilgan inactive

    def __str__(self):
        return f"{self.course_id.title} {self.price}"
