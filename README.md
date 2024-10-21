GUDLFT Booking App - README
This README will guide you through the process of setting up, running, and testing the GUDLFT booking app. Follow these instructions to start the application, run tests, and perform load testing using Locust.

1. Getting Started
Steps to start the app:
Clone the Repository: Download or clone the Git repository:

bash
Copy code
git clone <repository_url>
Navigate to the Project Directory: Open a terminal and position yourself inside the main folder of the project:

bash
Copy code
cd <project_directory>
Create a Virtual Environment: Create a virtual environment to isolate the project’s dependencies:

bash
Copy code
python3 -m venv venv
Activate the Virtual Environment:

On macOS and Linux:
bash
Copy code
source venv/bin/activate
On Windows:
bash
Copy code
venv\Scripts\activate
Install Dependencies: Install the required dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Set the Flask App Environment Variable: Specify the entry point for the Flask application by setting the FLASK_APP environment variable:

bash
Copy code
export FLASK_APP=server.py
Run the Flask App: Start the Flask app with the following command:

bash
Copy code
flask run
Access the Application: Open your browser and visit the following address to interact with the app:

arduino
Copy code
http://127.0.0.1:5000
2. Running Tests
Running All Tests with Pytest:
Pytest is used to run the test suite. To run all the tests, follow these steps:

Make sure you are in the main directory of the project.

Run the tests with the following command:

bash
Copy code
PYTHONPATH=. pytest
This command will run all the tests available in the project. You can also get detailed information on the test execution by using:

bash
Copy code
PYTHONPATH=. pytest -v
3. Load Testing with Locust
Steps to Perform Load Testing:
Ensure the Flask App is Not Running: The Flask app must NOT be running before starting Locust. This is necessary so Locust can properly initialize files.

Run Locust: Start the Locust load testing tool with the following command:

bash
Copy code
locust -f locust.py
Start the Flask App: After Locust is initialized, start the Flask app:

bash
Copy code
flask run
Access Locust's Web Interface: Open your browser and visit Locust's web interface at the following address:

arduino
Copy code
http://0.0.0.0:8089
Configure Load Test Parameters:

Set the number of users: 10 different clubs have been created for testing purposes.

Set the ramp-up time (how quickly users are added).

Set the host to point to the Flask app:

arduino
Copy code
http://127.0.0.1:5000
Start the Load Test: Once you've set the parameters, press the "Start" button to begin the load test.

4. Test Coverage Report
A coverage report is available to analyze the extent of test coverage. After running your tests, you can view the coverage report as follows:

Locate the Coverage Report: The report will be generated in the htmlcov folder.

Open the Coverage Report in a Browser: Open the index.html file in your browser to view the report:

bash
Copy code
open htmlcov/index.html
This report provides detailed insights into how much of your code is covered by tests.