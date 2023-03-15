from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.payment.models import Payment
from apps.payment.api.serializers import PaymentSerializer
from apps.payment.api.permissions import IsPaymentOwner
from apps.users.api.permissions import IsAuthDone
from apps.common.paginations import CustomPagination


class PaymentDetailAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    permission_classes = [IsPaymentOwner]


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer

    permission_classes = [IsAuthDone]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return user.course_payments.all()
