import pytest

from django.contrib.auth import get_user_model
from django.conf import settings


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


@pytest.mark.django_db
def test_login_user(client):

    # create user
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    # login
    response = client.post(
        "/api/v1/users/token",
        {
            "email":"c@c.com",
            "password": "c"
        },
        content_type = "application/json"
    )

    assert response.status_code == 200
    assert response.data['refresh']
    assert response.data['access']
    assert response.cookies.get(
        settings.SIMPLE_JWT[
            'AUTH_COOKIE'
            ],
        )