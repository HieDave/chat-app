from django.urls import path
from .views import (
    MessageListView, 
    )

urlpatterns = [
    path('message/', MessageListView.as_view(), name='messagelist'),
    ]