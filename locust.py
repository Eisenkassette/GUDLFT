from locust import HttpUser, task, between
import random
import json

clubs_data = {
    "clubs": [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "2000"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "2000"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "2000"
        },
        {
            "name": "Sport Club",
            "email": "alice@sportclub.com",
            "points": "2000"
        },
        {
            "name": "Another Club",
            "email": "Someone@anotherclub.com",
            "points": "2000"
        },
        {
            "name": "Best Club",
            "email": "someperson@bestclub.com",
            "points": "2000"
        },
        {
            "name": "Club 999",
            "email": "Bob@club999.com",
            "points": "2000"
        },
        {
            "name": "Club of club",
            "email": "Mick@clubofclub.com",
            "points": "2000"
        },
        {
            "name": "Super Club",
            "email": "Larry@superclub.com",
            "points": "2000"
        },
        {
            "name": "Giga Club",
            "email": "Norton@gigaclub.com",
            "points": "2000"
        }
    ]
}

competitions_data ={
    "competitions": [
        {
            "name": "Spring Festival",
            "date": "2030-03-27 10:00:00",
            "numberOfPlaces": 20000
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]
}

def create_json_files():
    """Function to create or reset JSON files with sample data."""
    with open('clubs.json', 'w') as clubs_file:
        json.dump(clubs_data, clubs_file, indent=4)

    with open('competitions.json', 'w') as competitions_file:
        json.dump(competitions_data, competitions_file, indent=4)

    print('Test json files created')

create_json_files()


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    user_data = [
        {'email': 'john@simplylift.co', 'club': 'Simply Lift'},
        {'email': 'admin@irontemple.com', 'club': 'Iron Temple'},
        {'email': 'kate@shelifts.co.uk', 'club': 'She Lifts'},
        {'email': 'alice@sportclub.com', 'club': 'Sport Club'},
        {'email': 'Someone@anotherclub.com', 'club': 'Another Club'},
        {'email': 'someperson@bestclub.com', 'club': 'Best Club'},
        {'email': 'Bob@club999.com', 'club': 'Club 999'},
        {'email': 'Mick@clubofclub.com', 'club': 'Club of club'},
        {'email': 'Larry@superclub.com', 'club': 'Super Club'},
        {'email': 'Norton@gigaclub.com', 'club': 'Giga Club'}
    ]

    @task(1)
    def load_homepage(self):
        """Simulate loading the homepage."""
        response = self.client.get("/")


    @task(2)
    def login_with_valid_email(self):
        """Simulate a user trying to log in with a valid email."""
        user = random.choice(self.user_data)
        response = self.client.post("/showSummary", data={
            'email': user['email']
        })


    @task(3)
    def book_competition(self):
        """Simulate accessing a competition booking page."""
        competition = 'Spring Festival'
        user = random.choice(self.user_data)
        response = self.client.get(f"/book/{competition}/{user['club']}")


    @task(4)
    def purchase_places(self):
        """Simulate a user purchasing places."""
        competition = 'Spring Festival'
        user = random.choice(self.user_data)
        response = self.client.post("/purchasePlaces", data={
            'competition': competition,
            'club': user['club'],
            'places': 5
        })

