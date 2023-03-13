from django.urls import path

from apps.about.api.views import (
    FeedbackCreateAPIView,
    NotificationListAPIView,
    NotificationDetailAPIView,
    AdvertisementDetailAPIView,
    UseTermDetailAPIView,
    ContactDetailAPIView,
)


app_name = 'about'

urlpatterns = [
    path('feedbacks/create/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
    path('notifications/list/', NotificationListAPIView.as_view(), name='notification-list'),
    path('notifications/<int:pk>/detail/', NotificationDetailAPIView.as_view(), name='notification-detail'),

    path('advertisement/detail/', AdvertisementDetailAPIView.as_view(), name='advertisement-detail'),
    path('use-term/detail/', UseTermDetailAPIView.as_view(), name='use-term-detail'),
    path('contact/detail/', ContactDetailAPIView.as_view(), name='contact-detail'),
]
