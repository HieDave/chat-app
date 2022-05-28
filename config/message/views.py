from rest_framework import generics

from .serializers import MessageSerializer
from .models import Message



class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer