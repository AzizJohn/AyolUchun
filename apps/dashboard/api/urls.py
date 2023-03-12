from django.urls import path

from apps.dashboard.api.views import UserCabinetDetailAPIView


app_name = 'dashboard'

urlpatterns = [
    path('users/<int:pk>/cabinet-detail/', UserCabinetDetailAPIView.as_view(), name='cabinet-detail'),

]
