from rest_framework import serializers
from apps.about.models import Feedback, Notification


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'email', 'phone_number', 'message', )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'context', 'scheduled_at', 'created_at', 'modified_at')
