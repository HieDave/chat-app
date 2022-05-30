import pytest

from django.contrib.auth import get_user_model
from profiles.models import Profile
from inbox.models import Inbox

User = get_user_model()


@pytest.mark.django_db
def test_profile_model():

    inbox = Inbox.objects.create()

    assert inbox.id == 1
