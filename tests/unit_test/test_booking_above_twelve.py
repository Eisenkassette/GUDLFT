import pytest

def test_booking_more_than_twelve(client):
    loggedinclub_name = 'Simply Lift'
    competition_name = 'Fall Classic'

    places_to_book = 12 + 1

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"


def test_booking_less_than_twelve(client):
    loggedinclub_name = 'Simply Lift'
    competition_name = 'Fall Classic'

    places_to_book = 5

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"