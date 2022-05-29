import pytest

from django.contrib.auth import get_user_model
from message.serializers import MessageSerializer
from profiles.models import Profile
from inbox.models import Inbox

User = get_user_model()

@pytest.mark.django_db
def test_valid_message_serializer():

    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )
    profile = Profile.objects.create(
        user = user,
        name = "Dave",
        is_online = True
    )

    inbox = Inbox.objects.create()
    inbox.profiles.add(profile)


    valid_serializer_data = {
        "profile": "1",
        "message_text": "Hie",
        "inbox": "1"
    }

    serializer = MessageSerializer(
        data = valid_serializer_data,
    )

    assert serializer.is_valid(
        raise_exception = True
    )
    assert serializer.validated_data['profile'] == profile
    assert serializer.validated_data['message_text'] == valid_serializer_data['message_text']
    assert serializer.validated_data['inbox'] == inbox
