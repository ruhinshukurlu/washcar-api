from django.contrib import admin
from core.models import Company, Reservation, CompanyReview, CarType
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "user","address", "created_at"]
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["company", "user", "date", "time", "car_type"]


@admin.register(CompanyReview)
class CompanyReviewAdmin(admin.ModelAdmin):
    list_display = ["company", "user", "rating", "created_at"]


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "is_active"]