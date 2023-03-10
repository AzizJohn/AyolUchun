from rest_framework import serializers
from .models import *


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('full_text', 'phone')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone', 'message')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('name', 'context', 'is_viewed', 'user_id', 'scheduled_time')
