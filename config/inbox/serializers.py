from rest_framework import serializers

from .models import Inbox



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

        profiles = validated_data.pop("profiles")
        inbox = Inbox.objects.create(
            last_message = validated_data.get("last_message"),
        )
        for item in profiles:
            inbox.profiles.add(item)
        return inbox
