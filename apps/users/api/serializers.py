from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from phonenumber_field.serializerfields import PhoneNumberField

from apps.users.models import User
from apps.common.choices import PURCHASED


###########################################################################
# ==========================   REGISTRATION   =============================
###########################################################################
class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'auth_status')
        read_only_fields = ('auth_status', )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(instance.get_token())
        return data


class RegisterPhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone_number', )


class RegisterPasswordSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'password2', )

    def validate(self, data):

        if data['password'] != data['password2']:
            raise ValidationError({
                'error': 'Two passwords must be the same!'
            })

        return data


###########################################################################
# ==========================         =============================
###########################################################################

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'avatar', 'username', 'gender', 'birthdate', 'email',
            'country', 'region', 'address', 'postal_index', 'phone_number',
            'instagram_account', 'imkon_account', 'linkedin_account',
            'work_place', 'position', 'bio'
        )
        extra_kwargs = {
            'birthdate': {'required': True}
        }


class UserCabinetSerializer(serializers.ModelSerializer):
    courses_number = serializers.SerializerMethodField()
    comments_number = serializers.SerializerMethodField()
    certificates_number = serializers.SerializerMethodField()

    def get_courses_number(self, user):
        courses_number = user.user_payments.filter(payment_status=PURCHASED).count()
        return courses_number

    def get_comments_number(self, user):
        comments_number = user.lecture_comments.count()
        return comments_number

    def get_certificates_number(self, user):
        certificates_number = user.certificates.count()
        return certificates_number

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'age', 'avatar', 'country', 'region',
            'courses_number', 'comments_number', 'certificates_number',
            'work_place', 'position', 'bio',
        )
