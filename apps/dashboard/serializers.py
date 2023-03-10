from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        'first_name', 'last_name', 'avatar', 'username', 'password', 'role_id', 'profession', 'country', 'region',
        'address', 'postal_index', 'phone', 'instagram_account', 'imkon_account', 'linkedin_account', 'work_place',
        'bio', 'birthdate', 'email', 'email_confirmation_link', 'email_confirmation_status', 'gender')
