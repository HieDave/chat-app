from django.urls import path
from .views import (
    MessageListView, 
    MessageDetailView
    )

urlpatterns = [
    path('message/', MessageListView.as_view(), name='messagelist'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message'),
    ]