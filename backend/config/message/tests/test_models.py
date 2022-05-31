import pytest

from django.contrib.auth import get_user_model
from profiles.models import Profile
from message.models import Message
from inbox.models import Inbox

User = get_user_model()

@pytest.mark.django_db
def test_profile_model():
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

    message = Message.objects.create(
        profile = profile,
        message_text = "Hie",
        inbox = inbox
    )

    assert message.profile == profile
    assert message.message_text == "Hie"
    assert message.inbox == inbox