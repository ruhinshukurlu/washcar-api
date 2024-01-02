from rest_framework import serializers
from core.models import Company, Reservation


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["id", "user", "name", "coordinates", "logo", "address"]


class CompanyDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["id", "user", "name",'reservations', "coordinates", "logo", "address"]


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail']



class ReservationListSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail']