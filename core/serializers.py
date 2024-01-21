from rest_framework import serializers
from core.models import Company, Reservation, CompanyReview, CarType


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["id", "user", "name", "coordinates", "logo", "address"]


class CarTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = ['id','title']

class CompanyDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    available_car_types = CarTypeSerializer(many=True)
    class Meta:
        model = Company
        fields = ["id", "user", "name",'average_rating',"coordinates", "logo", "address", 'available_car_types']

    def get_average_rating(self, company):
        reviews = company.reviews.all()
        if reviews:
            total_rating = sum([review.rating for review in reviews])
            return total_rating / len(reviews)
        return 0



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail', 'car_registration_number']



class ReservationListSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    car_type = CarTypeSerializer()
    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail']


class ReservationDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'date', 'time']


class CompanyReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = CompanyReview
        fields = ['id', 'company', 'reservation', 'rating', 'text']

    def validate(self, data):

        if data['rating'] < 0 or data['rating'] > 5:
            raise serializers.ValidationError(detail="Rating should be between 0 - 5!")

        return super().validate(data)



class CompanyAvailableHoursSerializer(serializers.ModelSerializer):
    reservations = ReservationDateSerializer(many=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'reservations']