from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.about.models import Feedback, Notification, Advertisement, UseTerm, Contact
from apps.about.api.serializers import (
    FeedbackSerializer, NotificationSerializer, AdvertisementSerializer, UseTermSerializer, ContactSerializer,
)
from apps.about.services.utils import get_last_object, update_notification_view


# Create your views here.
class FeedbackCreateAPIView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class NotificationListAPIView(ListAPIView):
    queryset = Notification.objects.all().order_by('-scheduled_at')
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.get_unread_notifications(self.request.user)


class NotificationDetailAPIView(RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # a function to store information about that user viewed given notification
        update_notification_view(instance.id, request.user.id)

        return Response(serializer.data)


class AdvertisementDetailAPIView(RetrieveAPIView):
    serializer_class = AdvertisementSerializer

    def get_object(self):
        ad = get_last_object(Advertisement)
        if ad is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return ad


class UseTermDetailAPIView(RetrieveAPIView):
    serializer_class = UseTermSerializer

    def get_object(self):
        ad = get_last_object(UseTerm)
        if ad is None:
            # if nothing found
            return Response(status=status.HTTP_404_NOT_FOUND)
        return ad


class ContactDetailAPIView(RetrieveAPIView):
    serializer_class = ContactSerializer

    def get_object(self):
        ad = get_last_object(Contact)
        if ad is None:
            # if nothing found
            return Response(status=status.HTTP_404_NOT_FOUND)
        return ad
