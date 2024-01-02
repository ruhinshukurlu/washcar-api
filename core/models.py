from django.db import models
import uuid


class Company(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField("account.User", verbose_name="User", on_delete=models.CASCADE, related_name='company')
    name = models.CharField("Name", max_length=50)
    coordinates = models.JSONField("Coordinates")
    logo = models.ImageField("Logo", upload_to='logos/', blank=True, null=True)
    address = models.CharField("Address", max_length=50, blank=True, null=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_active = models.BooleanField("Is Active", default=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.name


class CompanyReview(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    company = models.ForeignKey("core.Company", verbose_name="Company", on_delete=models.CASCADE, related_name='reviews')
    reservation = models.OneToOneField("core.Reservation", verbose_name="Reservation", on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey("account.User", verbose_name="User", on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField("Rating", default=0)
    text = models.TextField("Text", blank=True, null=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_active = models.BooleanField("Is Active", default=True)

    def __str__(self) -> str:
        return self.company.name


class Reservation(models.Model):
    CAR_TYPE_CHOICES = (
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('minivan', 'Minivan'),
        ('pickup', 'Pickup'),
    )

    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.ForeignKey("account.User", verbose_name="User", on_delete=models.CASCADE, related_name='reservations')
    company = models.ForeignKey("core.Company", verbose_name="Company", on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField("Date")
    time = models.TimeField("Time")
    car_type = models.CharField("Car Type", choices=CAR_TYPE_CHOICES, default='sedan', max_length=50)
    detail = models.TextField("Detail", blank=True, null=True)

    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)
    is_active = models.BooleanField("Is Active", default=True)


    def __str__(self) -> str:
        return self.company.name + str(self.user) + str(self.date)
