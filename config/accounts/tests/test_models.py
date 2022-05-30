import pytest

from django.contrib.auth import get_user_model



User = get_user_model()


@pytest.mark.django_db
def test_user_model():

    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    assert user.id == 1
    assert user.email == "c@c.com"