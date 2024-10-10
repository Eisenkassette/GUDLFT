import pytest

def test_over_booking(client):
    loggedinclub_name = 'Simply Lift'
    competition_name = 'Fall Classic'

    places_to_book = 14

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"


def test_booking(client):
    loggedinclub_name = 'Simply Lift'
    competition_name = 'Fall Classic'

    places_to_book = 12

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"