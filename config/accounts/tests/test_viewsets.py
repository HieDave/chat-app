import pytest

from django.contrib.auth import get_user_model


User = get_user_model()

@pytest.mark.django_db
def test_register_user(client):

    response = client.post(
        "/api/v1/users/register",
        {
            "email":"c@c.com",
            "password": "c"
        },
        content_type = "application/json"
    )

    assert response.status_code == 201
    assert response.data['email'] == "c@c.com"
    assert User.objects.all().count() == 1
