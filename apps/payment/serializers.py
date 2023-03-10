from rest_framework import serializers
from .models import *


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('course_id', 'Payer_user_id', 'price', 'payment_type_id', 'payed_at', 'payment_status')
