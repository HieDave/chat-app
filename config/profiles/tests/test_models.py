import pytest

from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()

@pytest.mark.django_db
def test_profile_model():
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )
    profile = Profile(
        user = user,
        name = "Dave",
        is_online=True
    )
    profile.save()

    assert profile.user == user
    assert profile.name == "Dave"
    assert profile.is_online == True