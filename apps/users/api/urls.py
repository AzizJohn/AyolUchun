from django.urls import path

from apps.users.api.views import (
    # registration
    SignUpAPIView, RegisterPhoneAPIView, ResendCodeAPIView,
    RegisterCodeVerifyAPIView, RegisterPasswordAPIView,

    # cabinet
    UserCabinetDetailAPIView, UserUpdateAPIView
)


app_name = 'users'

urlpatterns = [
    # registration
    path('register/', SignUpAPIView.as_view(), name='register'),
    path('register-phone/', RegisterPhoneAPIView.as_view(), name='register-phone'),
    path('resend-code/', ResendCodeAPIView.as_view(), name='resend-code'),
    path('code-verify/', RegisterCodeVerifyAPIView.as_view(), name='code-verify'),
    path('register-password/', RegisterPasswordAPIView.as_view(), name='register-password'),

    # cabinet
    path('cabinet-detail/', UserCabinetDetailAPIView.as_view(), name='cabinet-detail'),
    path('update/', UserUpdateAPIView.as_view(), name='user-update'),

]
