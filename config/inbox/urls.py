from django.urls import path
from .views import InboxListView

urlpatterns = [
    path('inbox', InboxListView.as_view(), name='inboxlist'),
    ]