from rest_framework import serializers
from core.models import Company, Reservation, CompanyReview


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ["id", "user", "name", "coordinates", "logo", "address"]


class CompanyDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = ["id", "user", "name",'average_rating',"coordinates", "logo", "address"]

    def get_average_rating(self, company):
        reviews = company.reviews.all()
        if reviews:
            total_rating = sum([review.rating for review in reviews])
            return total_rating / len(reviews)
        return 0


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail']



class ReservationListSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Reservation
        fields = ['id', 'company', 'date', 'time', 'car_type', 'detail']


class CompanyReviewSerilizer(serializers.ModelSerializer):

    class Meta:
        model = CompanyReview
        fields = ['id', 'company', 'reservation', 'rating', 'text']

    def validate(self, data):

        if data['rating'] < 0 or data['rating'] > 5:
            raise serializers.ValidationError(detail="Rating should be between 0 - 5!")

        return super().validate(data)