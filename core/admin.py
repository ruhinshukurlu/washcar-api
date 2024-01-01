from django.contrib import admin
from core.models import Company, Reservation
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

@admin.register(Company)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

admin.site.register(Reservation)
