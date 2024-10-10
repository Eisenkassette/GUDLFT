import pytest

def test_over_booking(client, mocker, mock_clubs, mock_competitions):
    mocker.patch('server.loadClubs', return_value=mock_clubs)
    mocker.patch('server.loadCompetitions', return_value=mock_competitions)

    loggedinclub_name = mock_clubs[0]['name']
    competition_name = mock_competitions[0]['name']

    places_to_book = int(mock_clubs[0]['points']) + 1

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"


def test_booking(client, mocker, mock_clubs, mock_competitions):
    mocker.patch('server.loadClubs', return_value=mock_clubs)
    mocker.patch('server.loadCompetitions', return_value=mock_competitions)

    loggedinclub_name = mock_clubs[0]['name']
    competition_name = mock_competitions[0]['name']

    places_to_book = int(mock_clubs[0]['points'])

    # POST request to the purchasePlaces endpoint
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })

    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"