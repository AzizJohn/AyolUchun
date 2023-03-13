from django.urls import path

from apps.users.api.views import UserCabinetDetailAPIView


app_name = 'users'

urlpatterns = [
    path('users/<int:pk>/cabinet-detail/', UserCabinetDetailAPIView.as_view(), name='cabinet-detail'),

]
