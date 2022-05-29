import pytest

from django.contrib.auth import get_user_model
from message.models import Message
from profiles.models import Profile
from inbox.models import Inbox

User = get_user_model()

@pytest.mark.django_db
def test_add_message(client):

    messages = Message.objects.all()
    assert messages.count() == 0

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

    response = client.post(
        "/api/v1/message/",
        {
            "profile": "1",
            "message_text": "Hie",
            "inbox": "1"
        },
        content_type = "application/json"
    )

    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['profile'] == 1
    assert response.data['message_text'] == "Hie"
    assert response.data['inbox'] == 1

    messages = Message.objects.all()
    assert messages.count() == 1

    #check that inbox last_message field is updated
    inbox = Inbox.objects.get(id=1)
    assert inbox.last_message == Message.objects.get(id = 1)

@pytest.mark.django_db
def test_retreive_messages(client):
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

    response = client.post(
        "/api/v1/message/",
        {
            "profile": "1",
            "message_text": "Hie",
            "inbox": "1"
        },
        content_type = "application/json"
    )

    assert response.status_code == 201

    response_data = response.data

    response = client.get(
        f"/api/v1/message/",
    )

    assert response.status_code == 200
