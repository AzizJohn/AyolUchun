from django.urls import path

from apps.payment.api.views import PaymentDetailAPIView, PaymentListAPIView


app_name = 'payment'

urlpatterns = [
    path('list/', PaymentListAPIView.as_view(), name='payment-list'),
    path('<int:pk>/detail/', PaymentDetailAPIView.as_view(), name='payment-detail'),

]
