from rest_framework import generics

from .serializers import InboxSerializer
from .models import Inbox

# Create your views here.
class InboxListView(generics.ListAPIView):
    queryset = Inbox.objects.all()
    serializer_class = InboxSerializer