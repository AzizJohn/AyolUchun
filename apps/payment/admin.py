from django.contrib import admin

# Register your models here.
from apps.payment.models import Payment

admin.site.register(Payment)
