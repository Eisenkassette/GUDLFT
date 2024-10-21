import pytest

def test_full_path(client, mock_data):
    loggedinclub_email = "john@simplylift.co"
    loggedinclub_name = 'Simply Lift'
    original_points = 13
    competition_name = 'Spring Festival'
    places_to_book = 5
    original_places = 25

    # Loggin as a valid user
    response = client.post('/showSummary', data={'email': loggedinclub_email})
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Accessing the booking page of an upcoming competition
    response = client.get(f'/book/{competition_name}/{loggedinclub_name}')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Book a legal ammount of places to an upcoming event
    response = client.post('/purchasePlaces', data={
        'club': loggedinclub_name,
        'competition': competition_name,
        'places': places_to_book
    })
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    club = next(club for club in mock_data['clubs'] if club['name'] == loggedinclub_name)
    updated_points = int(club['points'])  # Get updated points after booking
    competition = next(competition for competition in mock_data['competitions'] if competition['name'] == competition_name)
    updated_places = int(competition['numberOfPlaces'])  # Get updated number of places after booking
    # Assert that the club's available points have been updated correctly
    assert updated_points  == (original_points - places_to_book), \
        f"Expected {original_points - places_to_book} club points, but got {updated_points}"
    # Assert that the competition's number of places has been updated correctly
    assert updated_places == (original_places - places_to_book), \
        f"Expected {original_places - places_to_book} competition places, but got {updated_places}"

    # Go to the clubsinfo page
    response = client.get('/clubsinfo')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Logout
    response = client.get('/clubsinfo')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"