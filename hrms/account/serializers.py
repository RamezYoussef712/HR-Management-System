from rest_framework import serializers
from .models import User
from datetime import datetime
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    # confirm_password = serializers.CharField(write_only=True)

    company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    department = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'hire_date', 'start_date',
                  'end_date', 'company', 'department']

    def validate_start_date(self, value):
        entered_end_date = self.initial_data.get('end_date')
        parsed_end_date = datetime.strptime(entered_end_date, "%Y-%m-%d").date()
        if value > parsed_end_date:
            raise serializers.ValidationError({'details': 'End date must be after start date.'})
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password', 'first_name', 'last_name', 'company',
                  'department']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self, **kwargs):
        user = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username'),
            password=self.validated_data.get('password'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            company=self.validated_data.get('company'),
            department=self.validated_data.get('department'),
        )
        if self.validated_data.get('password') != self.validated_data.get('confirm_password'):
            raise serializers.ValidationError({'details': 'passwords did not match'})
        user.set_password(self.validated_data.get('password'))
        user.save()
        token = Token.objects.create(user=user)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    department = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'company',
                  'department']
        read_only_fields = ['company', 'department']
