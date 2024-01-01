from rest_framework import serializers
from core.models import Company, Reservation


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["id", "user", "name", "coordinates", "logo", "address"]