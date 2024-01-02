from django.urls import path
from core.views import *

app_name = 'core'

urlpatterns = [
    path('company/list/',CompanyListView.as_view(), name='company-list'),
    path('company/create/',CompanyCreateAPIView.as_view(), name='company-create'),
    path('company/<uuid:id>/',CompanyDetailApiView.as_view(), name='company-detail'),

    path('reservations/create', CreateReservationApiView.as_view(), name='create-reservation'),
    path('reservations/list/', ReservationListApiView.as_view(), name='reservation-list')
]
