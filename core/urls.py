from django.urls import path
from core.views import CompanyListView, CompanyCreateAPIView

app_name = 'core'

urlpatterns = [
    path('company/list',CompanyListView.as_view(), name='company-list'),
    path('company/create',CompanyCreateAPIView.as_view(), name='company-create'),
]
