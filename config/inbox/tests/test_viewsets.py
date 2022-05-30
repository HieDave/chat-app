import pytest

from django.contrib.auth import get_user_model
from inbox.models import Inbox
from profiles.models import Profile
from inbox.models import Inbox

User = get_user_model()

@pytest.mark.django_db
def test_add_inbox(client):

    #create first profile
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )
    profile = Profile.objects.create(
        user = user,
        name = "Dave",
        is_online = True
    )

    # create second profile
    user = User.objects.create_user(
        email = "d@d.com",
        password = "d"
    )
    profile = Profile.objects.create(
        user = user,
        name = "Dave",
        is_online = True
    )

    # create inbox with those users
    response = client.post(
        "/api/v1/inbox",
        {
            "profiles": [1,2],
        },
        content_type = "application/json"
    )

    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['profiles'] == [1,2]

    inbox = Inbox.objects.all()
    assert inbox.count() == 1

@pytest.mark.django_db
def test_retreive_inbox(client):
    #create inbox
    inbox = Inbox.objects.create()

    #create first profile
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )
    profile = Profile.objects.create(
        user = user,
        name = "Dave",
        is_online = True
    )

    # add profile to inbox
    inbox.profiles.add(profile)

    # create second profile
    user = User.objects.create_user(
        email = "d@d.com",
        password = "d"
    )
    profile = Profile.objects.create(
        user = user,
        name = "Dave",
        is_online = True
    )

    # add profile to inbox
    inbox.profiles.add(profile)


    # create inbox with those users
    response = client.get(
        "/api/v1/inbox",
    )

    assert response.status_code == 200