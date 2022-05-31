import pytest

from django.contrib.auth import get_user_model
from inbox.serializers import ReadInboxSerializer, WriteInboxSerializer
from profiles.models import Profile
from inbox.models import Inbox


User = get_user_model()

@pytest.mark.django_db
def test_valid_inbox_serializer():

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
    valid_serializer_data = {
        "profiles": [1,2]
    }

    serializer = WriteInboxSerializer(
        data = valid_serializer_data
    )

    assert serializer.is_valid(
        raise_exception = True
    )
    assert serializer.validated_data['profiles'][0].id == 1
    assert serializer.validated_data['profiles'][1].id == 2



