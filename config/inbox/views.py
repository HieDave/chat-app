from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import SAFE_METHODS
from rest_framework import filters
from rest_framework import generics

from .serializers import ReadInboxSerializer, WriteInboxSerializer
from .models import Inbox



class InboxListView(generics.ListCreateAPIView):
    queryset = Inbox.objects.all()
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter
        ]
    filterset_fields = ['id', 'users', 'last_message']
    ordering_fields = '__all__'
    ordering = ['id']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ReadInboxSerializer
        return WriteInboxSerializer