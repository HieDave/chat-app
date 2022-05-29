import pytest

from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()


@pytest.mark.django_db
def test_add_profile(client):
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    profiles = Profile.objects.all()
    assert profiles.count() == 0

    response = client.post(
        "/api/v1/profile/",
        {
            "user": "1",
            "name": "Dave",
            "is_online": "True"
        },
        content_type = "application/json"
    )

    assert response.status_code == 201
    assert response.data['id'] == 1
    assert response.data['user'] == 1
    assert response.data['name'] == "Dave"
    assert response.data['is_online'] == True


    profiles = Profile.objects.all()
    assert profiles.count() == 1

@pytest.mark.django_db
def test_retrieve_profile(client):
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    response = client.post(
        "/api/v1/profile/",
        {
            "user": "1",
            "name": "Dave",
            "is_online": "True"
        },
        content_type="application/json"
    )

    assert response.status_code == 201

    response_data = response.data

    response = client.get(
        f"/api/v1/profile/{response_data['id']}/",
    )

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_profile(client):
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    response = client.post(
        "/api/v1/profile/",
        {
            "user": "1",
            "name": "Dave",
            "is_online": "True"
        },
        content_type="application/json"
    )

    assert response.status_code == 201

    response_data = response.data

    response = client.patch(
        f"/api/v1/profile/{response_data['id']}/",
        {
            "name": "John",
        },
        content_type="application/json"
    )

    assert response.status_code == 200
    assert response.data['id'] == 1
    assert response.data['user'] == 1
    assert response.data['name'] == "John"
    assert response.data['is_online'] == True


@pytest.mark.django_db
def test_delete_profile(client):
    user = User.objects.create_user(
        email = "c@c.com",
        password = "c"
    )

    response = client.post(
        "/api/v1/profile/",
        {
            "user": "1",
            "name": "Dave",
            "is_online": "True"
        },
        content_type="application/json"
    )

    assert response.status_code == 201

    response_data = response.data

    response = client.delete(
        f"/api/v1/profile/{response_data['id']}/",
    )

    assert response.status_code == 204
