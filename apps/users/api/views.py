from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserCabinetSerializer


class UserCabinetDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCabinetSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
