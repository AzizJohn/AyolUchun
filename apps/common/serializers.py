from rest_framework import serializers
from apps.common.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id', 'profile_pic', 'gender', 'first_name', 'last_name',
            'email', 'bio', 'created_at', 'updated_at',
        )
