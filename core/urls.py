from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import ListUsers

app_name = 'core'

urlpatterns = [
    path('',ListUsers.as_view(), name='home'),
]
