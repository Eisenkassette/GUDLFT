import pytest

def test_access_booking_closed_competition(client):

    loggedinclub_name = 'Simply Lift'
    competition_name = 'Fall Classic'

    # GET request to the booking endpoint
    response = client.get(f'/book/{competition_name}/{loggedinclub_name}')

    assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"


def test_access_booking_upcoming_competition(client):
    loggedinclub_name = 'Simply Lift'
    competition_name = 'Spring Festival'

    # GET request to the booking endpoint
    response = client.get(f'/book/{competition_name}/{loggedinclub_name}')

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"