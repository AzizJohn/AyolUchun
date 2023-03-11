from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView

from apps.about.models import Feedback, Notification, Advertisement, UseTerm, Contact
from apps.about.serializers import (
    FeedbackSerializer, NotificationSerializer, AdvertisementSerializer, UseTermSerializer, ContactSerializer,
)


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


