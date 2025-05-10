**Senior QA Automation Engineer Practical Assessment
Overview**


This solution uses Playwright with Page Object Model for UI automation, Python for scripting, and Docker for containerization. 
I've also added some API tests just for POC.

**Prerequisites**
Before running the tests, ensure the following are installed on your system:

Docker: To run the demo application locally.

Python 3.8+: To execute the test scripts.

Playwright: To run browser automation.

pytest: To execute the tests and generate reports.

dotenv: For loading environment variables.

Setup:
1. Clone the repo
2. Make sure you are in the root directory of the project 
3. install dependencies:

`pip3 install -r requirements.txt`


Environment Setup

Set up Docker:

1. Ensure that Docker is installed and running on your local machine.
2. Make sure the app is running locally



Running the Tests

Run All tests (UI and API) in headless mode

`pytest -v`

Run a specific test using pytest mark, make sure the test has a mark

`pytest -v -m edit_article`

Run a specific test using pytest mark, headed mode

`pytest -v -m edit_article --headless-toggle`

Tests Included

**API**

1. Sign-up & Login (positive and negative cases):
   - Register a new user.
   - Log in successfully.
   - Attempt login with an incorrect password, expecting an error message. It has two parameters just to show how it can 
   work with different inputs


**UI**


1. Create a new article

2. Ensure the article appears in the "My Articles" list.

3. Follow Feed:

User A follows User B.

User B publishes a new article.

Verify that the new article appears in User A's feed.

Additional tests cover:

1. Edit / Delete Article: Author can update and delete articles.

2. Favourite Toggle: Favourite/unfavourite an article


Docker Configuration
To run the solution in a containerized environment using Docker, follow these steps:

Build the Docker images:

`docker build -t playwright-tests .`


Run the tests in Docker:

 `docker run --rm playwright-tests`
 
Additional comments:
1. Added some utilities to help creating new users when running in local env
2. Added some utilities to help creating new articles when running in local env