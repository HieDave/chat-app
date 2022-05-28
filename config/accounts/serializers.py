from django.contrib.auth import get_user_model
from profiles.serializers import ProfileSerializer

from rest_framework import serializers



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = [
            'id', 
            'email', 
            'password',
            'profile'
            ]