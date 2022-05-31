import pytest

from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer


User = get_user_model()

@pytest.mark.django_db
def test_user_serializer():

    valid_serializer_data = {
        "email": "c@c.com",
        "password": "c"
    }

    serializer = UserSerializer(
        data = valid_serializer_data,
    )

    assert serializer.is_valid(
        raise_exception = True
    )
    assert serializer.validated_data['email'] == valid_serializer_data['email']
    assert serializer.validated_data['password'] == valid_serializer_data['password']
