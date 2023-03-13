from rest_framework.generics import RetrieveAPIView

from apps.dashboard.models import User
from apps.dashboard.api.serializers import UserSerializer, UserCabinetSerializer


class UserCabinetDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCabinetSerializer
