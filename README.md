# GUDLFT Booking App - README

This README will guide you through the process of setting up, running, and testing the GUDLFT booking app. Follow these instructions to start the application, run tests, and perform load testing using Locust.

## 1. Getting Started

### Steps to start the app:

1. **Clone the Repository:**
   Download or clone the QA Git repository:

   ```bash
   git clone -b QA https://github.com/Eisenkassette/GUDLFT --single-branch
   ```

2. **Navigate to the Project Directory:**
   Open a terminal and position yourself inside the main folder of the project:

   ```bash
   cd <project_directory>
   ```

3. **Create a Virtual Environment:**
   Create a virtual environment to isolate the project’s dependencies:

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

5. **Install Dependencies:**
   Install the required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

6. **Set the Flask App Environment Variable:**
   Specify the entry point for the Flask application by setting the `FLASK_APP` environment variable:

   ```bash
   export FLASK_APP=server.py
   ```

7. **Run the Flask App:**
   Start the Flask app with the following command:

   ```bash
   flask run
   ```

8. **Access the Application:**
   Open your browser and visit the following address to interact with the app:

   ```
   http://127.0.0.1:5000
   ```

## 2. Running Tests

### Running All Tests with Pytest:

Pytest is used to run the test suite. To run all the tests, follow these steps:

1. Make sure you are in the main directory of the project.
2. Run the tests with the following command:

   ```bash
   PYTHONPATH=. pytest
   ```

This command will run all the tests available in the project. You can also get detailed information on the test execution by using:

```bash
PYTHONPATH=. pytest -v
```

## 3. Load Testing with Locust

### Steps to Perform Load Testing:

1. **Ensure the Flask App is Not Running:**
   The Flask app must **NOT** be running before starting Locust. This is necessary so Flask can initialize testing json files.

2. **Run Locust:**
   Start the Locust load testing tool with the following command:

   ```bash
   locust -f locust.py
   ```

3. **Start the Flask App:**
   After Locust is initialized, start the Flask app:

   ```bash
   flask run
   ```

4. **Access Locust's Web Interface:**
   Open your browser and visit Locust's web interface at the following address:

   ```
   http://0.0.0.0:8089
   ```

5. **Configure Load Test Parameters:**
   - Set the **number of users**: 10 different clubs have been created for testing purposes.
   - Set the **ramp-up time** (how quickly users are added).
   - Set the **host** to point to the Flask app:

     ```
     http://127.0.0.1:5000
     ```

6. **Start the Load Test:**
   Once you've set the parameters, press the "Start" button to begin the load test.

## 4. Test Coverage Report

A coverage report is available to analyze the extent of test coverage.

1. **Locate the Coverage Report:**
   The report will be in the `htmlcov` folder.

2. **Open the Coverage Report in a Browser:**
   Open the `index.html` file in your browser to view the report.

This report provides detailed insights into how much of your code is covered by tests.
