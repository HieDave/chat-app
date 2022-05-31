import pytest

from django.contrib.auth import get_user_model
from profiles.serializers import ProfileSerializer

User = get_user_model()

@pytest.mark.django_db
def test_valid_profile_serializer():

    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    valid_serializer_data = {
        "user": "1",
        "name": "Dave",
        "is_online": True
    }

    serializer = ProfileSerializer(
        data = valid_serializer_data,
    )


    assert serializer.is_valid(
        raise_exception = True
    )
    assert serializer.validated_data['user'] == user
    assert serializer.validated_data['name'] == valid_serializer_data['name']
    assert serializer.validated_data['is_online'] == valid_serializer_data['is_online']
