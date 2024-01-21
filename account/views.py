from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from account.utils import jwt_decode_handler
from account.serializer import UserSerializer, UserCreateSerializer, CustomTokenObtainSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """Register view for the users."""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    # serializer_class = CustomTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        data = super().post( request, *args, **kwargs)

        data = data.data

        access_token = jwt_decode_handler(data.get("access"))
        user = User.objects.filter(phone_number=access_token.get("phone_number")).first()
        print("login")
        if not user:
            return Response({"error":True, "message":"No such user!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)

        data["user"] = serializer.data

        return Response(data)


class UserProfileView(views.APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        current_user = self.request.user
        user = User.objects.get(phone_number=current_user)
        return Response(UserSerializer(user).data)