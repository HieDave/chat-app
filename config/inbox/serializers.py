from rest_framework import serializers
from accounts.serializers import UserSerializer
from message.serializers import MessageSerializer

from .models import Inbox


class InboxSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    last_message = MessageSerializer()

    class Meta:
        model = Inbox
        fields = '__all__'