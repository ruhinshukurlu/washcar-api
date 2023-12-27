from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import LoginView, RegisterView, UserProfileView

app_name = 'account'

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/',UserProfileView.as_view(), name='user'),
]
