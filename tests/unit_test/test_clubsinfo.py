import pytest


def test_route_clubsinfo(client):
    # GET request to the clubsinfo endpoint
    response = client.get('/clubsinfo')

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
