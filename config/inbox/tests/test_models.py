import pytest

from inbox.models import Inbox




@pytest.mark.django_db
def test_profile_model():

    inbox = Inbox.objects.create()

    assert inbox.id == 1
