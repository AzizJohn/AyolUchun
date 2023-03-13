from django.urls import path

from apps.users.api.views import UserCabinetDetailAPIView, UserUpdateAPIView


app_name = 'users'

urlpatterns = [
    path('<int:pk>/cabinet-detail/', UserCabinetDetailAPIView.as_view(), name='cabinet-detail'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),

]
