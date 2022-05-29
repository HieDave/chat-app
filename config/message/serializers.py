from rest_framework import serializers

from .models import Message
from inbox.models import Inbox


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'

    def create(self, validated_data):
        inbox = validated_data.get('inbox')
        message = Message.objects.create(
            profile = validated_data['profile'],
            message_text = validated_data['message_text'],
            inbox = validated_data['inbox']
        )

        # update last message field in inbox table
        Inbox.objects.filter(
            id=inbox.id
            ).update(
                last_message = message.id 
            )
        
        return message
  