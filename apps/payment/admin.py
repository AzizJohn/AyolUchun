from django.contrib import admin

from apps.payment.models import Payment


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'payer', 'price', 'payed_at')


admin.site.register(Payment, PaymentAdmin)
