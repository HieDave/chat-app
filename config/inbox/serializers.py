from rest_framework import serializers
from accounts.serializers import UserSerializer
from message.serializers import MessageSerializer

from django.contrib.auth import get_user_model

from .models import Inbox



User = get_user_model()

class ReadInboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbox
        fields = '__all__'
        depth = 2


class WriteInboxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inbox
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        users = validated_data.pop("users")
        inbox = Inbox.objects.create(
            last_message = validated_data["last_message"],
        )
        for item in users:
            inbox.users.add(item)
        return inbox
