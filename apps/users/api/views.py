from django.utils import timezone

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserCabinetSerializer, SignUpSerializer, RegisterPhoneSerializer
from apps.users.services.message_sender import send_confirmation_code
from apps.common.choices import PHONE_ENTERED


###########################################################################
# =======================   REGISTRATION VIEWS   =========================
###########################################################################
class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class RegisterPhoneAPIView(APIView):

    def post(self, request):
        serializer = RegisterPhoneSerializer(data=request.data)

        if serializer.is_valid():
            # get objects
            data = serializer.validated_data
            phone_number = data['phone_number']
            user = request.user

            # change user field values
            user.phone_number = phone_number
            user.auth_status = PHONE_ENTERED
            user.save()

            # send verification code sms
            now = timezone.now()
            if user.confirmation_codes.filter(is_confirmed=False, expired_at__gte=now).exists():
                # return error message, if code already exists in database
                return Response(
                    data={"error": "Verification code has already been sent!"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            code = user.create_phone_verify_code()
            send_confirmation_code(phone_number, code)

            # return response
            data.update(auth_status=user.auth_status)
            return Response(data=data, status=status.HTTP_200_OK)

        # return response with validation errors in serializer
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCodeVerifyAPIView(APIView):

    def post(self, request):
        # get necessary objects
        code = request.data.get('code')
        user = request.user

        # codes =


###########################################################################
# =======================      VIEWS   =========================
###########################################################################

class UserCabinetDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCabinetSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
