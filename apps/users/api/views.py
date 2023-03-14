from django.utils import timezone
from django.db.models import Q

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import User
from apps.users.api.serializers import (
    UserSerializer, UserCabinetSerializer,
    SignUpSerializer, RegisterPhoneSerializer, RegisterPasswordSerializer
)
from apps.users.services.message_sender import send_confirmation_code
from apps.common.choices import PHONE_ENTERED, CODE_VERIFIED, AUTH_DONE


###########################################################################
# =======================   REGISTRATION VIEWS   =========================
###########################################################################
class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class RegisterPhoneAPIView(APIView):

    def post(self, request):
        serializer = RegisterPhoneSerializer(data=request.data)

        # get objects
        phone_number = request.data.get("phone_number")
        user = request.user

        # check user already exists
        registered_users = User.objects.filter(phone_number=phone_number).exclude(auth_status=AUTH_DONE)
        if registered_users.exists():
            registered_users.delete()

        if serializer.is_valid():
            data = serializer.data

            # change user field values
            user.phone_number = phone_number
            user.auth_status = PHONE_ENTERED
            user.save()

            # send verification code sms
            now = timezone.now()
            if user.confirmation_codes.filter(is_confirmed=False, expired_at__gte=now).exists():
                # return error message, if code already exists in database
                return Response(
                    data={"error": "Verification code has already been sent!", "auth_status": user.auth_status},
                    status=status.HTTP_400_BAD_REQUEST
                )
            code = user.create_phone_verify_code()
            send_confirmation_code(phone_number, code)

            # return response
            data.update({'auth_status': user.auth_status})
            return Response(data=data, status=status.HTTP_200_OK)

        # return response with validation errors in serializer
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterCodeVerifyAPIView(APIView):

    def post(self, request):
        # get necessary objects
        code = request.data.get('code')
        user = request.user

        # check if such code exists for this user
        match_codes = user.confirmation_codes.filter(code=code, is_confirmed=False)

        if match_codes.exists():
            # check if this code is not expired
            now = timezone.now()
            valid_codes = match_codes.filter(expired_at__gte=now)

            if valid_codes.exists():
                # change user status
                user.auth_status = CODE_VERIFIED
                user.save()
                # change code is_confirmed field to True

                # Correct code, return Success Response
                return Response(
                    data={"auth_status": user.auth_status},
                    status=status.HTTP_200_OK
                )

            # if code entered is expired, return error message
            return Response(
                data={'code': 'Code entered is expired!'}
            )

        # Incorrect code entered, return error
        return Response(
            data={'code': 'Incorrect code entered!', "auth_status": user.auth_status},
            status=status.HTTP_400_BAD_REQUEST
        )


class RegisterPasswordAPIView(APIView):

    def post(self, request):
        serializer = RegisterPasswordSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data['password']
            user = request.user

            user.set_password(password)
            user.auth_status = AUTH_DONE
            user.save()

            return Response(
                data={'message': 'Your registration completed successfully!'},
                status=status.HTTP_200_OK
            )

        # return validation error message in serializer
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########################################################################
# =======================    VIEWS   =========================
###########################################################################

class UserCabinetDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCabinetSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
