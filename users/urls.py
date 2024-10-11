from django.urls import path

from users.apps import UsersConfig
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserListAPIView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
