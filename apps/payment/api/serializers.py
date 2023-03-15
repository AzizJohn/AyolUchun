from rest_framework import serializers

from apps.payment.models import Payment
from apps.course.serializers import CourseSerializer


class PaymentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = (
            'course', 'payer', 'price', 'payment_type', 'payment_status',
            'payed_at', 'created_at', 'updated_at',
        )
