from django.urls import path
from .views import (
    ProfileListView, 
    ProfileDetailView
    )

urlpatterns = [
    path('profile/', ProfileListView.as_view(), name='profilelist'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    ] 