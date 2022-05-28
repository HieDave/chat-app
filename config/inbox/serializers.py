from rest_framework import serializers
from accounts.serializers import UserSerializer
from message.serializers import MessageSerializer

from django.contrib.auth import get_user_model

from .models import Inbox
from .models import Inbox_participants


User = get_user_model()

class ReadInboxSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    last_message = MessageSerializer()

    class Meta:
        model = Inbox
        fields = '__all__'



class Inbox_participantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox_participants
        fields = '__all__'

class WriteInboxSerializer(serializers.ModelSerializer):
    users = serializers.ListField(write_only=True)

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
            user_object = User.objects.get(id=item)
            Inbox_participants.objects.create(
                user = user_object, 
                inbox = inbox
                )
        return inbox
