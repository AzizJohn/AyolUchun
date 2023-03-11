from rest_framework import serializers
from apps.about.models import Feedback, Notification, Advertisement, UseTerm, Contact


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'name', 'email', 'phone_number', 'message', )


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'context', 'scheduled_at', 'created_at', 'updated_at')


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'image', 'content', 'phone_number',)


class UseTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseTerm
        fields = ('id', 'title', 'image', 'content',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone_number', 'email', 'address', 'long', 'lat', )
