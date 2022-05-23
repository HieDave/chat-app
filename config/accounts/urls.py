from django.urls import path

from .views import (
    UserRegisterView,
    UserLoginView,
    RefreshTokenView,
    UserLogoutView 
    )


urlpatterns = [
    path('users/register', UserRegisterView.as_view(), name='register'),
    path('users/token', UserLoginView.as_view(), name='login'),
    path('users/token/refresh', RefreshTokenView.as_view(), name='refresh'),
    path('users/logout', UserLogoutView.as_view(), name='logout'),
]