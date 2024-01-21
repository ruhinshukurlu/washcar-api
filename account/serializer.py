from typing import Any, Dict, Optional, Type, TypeVar

from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class CustomAuthFailedExcetion(AuthenticationFailed):
    status_code = HTTP_404_NOT_FOUND

class CustomTokenObtainSerializer(TokenObtainSerializer):
    default_error_messages = {
        "no_active_account": "No active account found with the given credentials!!!"
    }

    def validate(self, attrs: Dict[str, Any]) -> Dict[Any, Any]:
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise CustomAuthFailedExcetion(
                self.error_messages["no_active_account"],
                "no_active_account",
            )

        return {}


class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):
    token_class = RefreshToken

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['fullname','phone_number']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators = [validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id','phone_number', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})
        return data

    def create(self, validated_data):

        user = User.objects.create(
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user