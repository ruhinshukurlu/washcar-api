from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from core.models import Company, Reservation
from core.serializers import *

class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (AllowAny, )


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny, )


class CompanyDetailApiView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyDetailSerializer
    permission_classes = (AllowAny, )
    lookup_field = 'id'


class CompanyReservations(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyAvailableHoursSerializer
    permission_classes = (AllowAny, )
    lookup_field = 'id'


class CreateReservationApiView(CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class ReservationListApiView(ListAPIView):
    """List of reservations for the logged in user, you should pass access_token in the headers for the authorization!!!"""
    queryset = Reservation.objects.all()
    serializer_class = ReservationListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        current_user = self.request.user
        return super().get_queryset().filter(user=current_user)


class CreateReviewApiView(CreateAPIView):
    queryset = CompanyReview.objects.all()
    serializer_class = CompanyReviewSerilizer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class CarTypeListApiView(ListAPIView):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
