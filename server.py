import json
import threading
import time
from flask import Flask,render_template,request,redirect,flash,url_for
# Added datetime to be able to check current against competition date.
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs

def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

# Function to periodically save data to json
def periodic_save():
    while True:
        time.sleep(60)

        with open('clubs.json', 'w') as clubs_file:
            json.dump({"clubs": clubs}, clubs_file, indent=4)

        with open('competitions.json', 'w') as competitions_file:
            json.dump({"competitions": competitions}, competitions_file, indent=4)

        print("Data saved to JSON files.")

def start_background_saving():
    thread = threading.Thread(target=periodic_save, daemon=True)
    thread.start()


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

start_background_saving()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    # Replaced full list search with next(), advantages:
    # - When a club with a matching email is found we stop scanning, making it more efficient
    # by reducing the amount of useless operations as one email should be unique to a club.
    # - If no matchs a found we won't get an index error, club will simple be equal to None
    # making the later check possible.
    club = next((club for club in clubs if club['email'] == request.form['email']), None)

    # Verification that ensure that we got a matching club to the provided email if not:
    # - Flash an "email not found" error message.
    # - Redirect to index.html for the user to see the message.
    if not club:
        flash('Email not found. Please try again.', 'error')
        return redirect(url_for('index'))

    return render_template('welcome.html',club=club,competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        current_date = datetime.now()
        competition_date = datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S')
        # Added a verification that checks if the competition has already taken place.
        # If the competition is a past one, sends back to welcome.html with an error message.
        if current_date > competition_date:
            flash("That competition is over.")
            return render_template('welcome.html', club=club, competitions=competitions), 403
        else:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    # Added verification that the clubs has not asked for more places than they have points
    # If they don't have enough points the user is redirected to the booking page.
    if placesRequired > int(club['points']):
        flash('You do not have a sufficient amount of points.', 'error')
        return redirect(request.referrer), 403
    # Aded a check in the case were the user tries to book more than 12 places redirect with error.
    elif placesRequired > 12:
        flash('You cannot book more than 12 places', 'error')
        return redirect(request.referrer), 403
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        # Added an update section for the club points.
        club_points = int(club['points'])
        club['points'] = str(club_points - placesRequired)
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


# Added new route to display all clubs info
@app.route('/clubsinfo')
def clubsinfo():
    return render_template('clubsinfo.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))