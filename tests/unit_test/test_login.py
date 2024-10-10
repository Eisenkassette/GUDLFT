import pytest

def test_login_with_valid_email(client):
    valid_email = "admin@irontemple.com"
    response = client.post('/showSummary', data={'email': valid_email})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_login_with_wrong_email(client):
    wrong_email = "thisemaildoesntexist@wrongemail.com"
    response = client.post('/showSummary', data={'email': wrong_email})
    assert response.status_code == 302, f"Expected status code 302, but got {response.status_code}"
