# **Senior QA Automation Engineer Practical Assessment

## Overview**


This solution uses Playwright with Page Object Model for UI automation, Python for scripting, and Docker for containerization. 
I've also added some API tests just for POC.

**SIDE NOTE:**
In the assessment it says that _Attempt login with a wrong password → expect HTTP 401 / error message_.
But the actual error is _422_, so the 2 API tests that are failing  - it's expected.

**Prerequisites**
Before running the tests, ensure the following are installed on your system:

Docker: To run the demo application locally.

Python 3.8+: To execute the test scripts.

Playwright: To run browser automation.

pytest: To execute the tests and generate reports.

dotenv: For loading environment variables.

**Setup:**
1. Clone the repo
2. Make sure you are in the root directory of the project 
3. install dependencies:

`pip3 install -r requirements.txt`


**Environment Setup**

Set up Docker:

1. Ensure that Docker is installed and running on your local machine.
2. Make sure the app is running locally



**Running the Tests**

Run All tests (UI and API) in headless mode

`pytest -v`

Run a specific test using pytest mark, make sure the test has a mark

`pytest -v -m edit_article`

Run a specific test using pytest mark, headed mode

`pytest -v -m edit_article --headless-toggle`

**Tests Included**

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





## **Docker Configuration**

To run the solution in a containerized environment using Docker, follow these steps:

Build the Docker images:

`docker build -t playwright-tests .`


Run the tests in Docker:

 `docker run --rm playwright-tests`
 
Additional comments:
1. Added some utilities to help create new users when running in local env
2. Added some utilities to help create new articles when running in local env


## **Assessment checklist:**
- [x] You should develop and test against the application running locally via Docker.
- [x] Core user journeys – all required 
Sign-up & Login

• Register a new user

• Log in successfully

• Attempt login with a wrong password → expect HTTP 401 / error message
Done via API tests. In the assessment it does not say anything about API tests, only UI, I've just decided to take this 
initiave and write a few API tests.

- [x] Write Article

• Logged-in user creates an article (title, body, tags)

• Article appears in “My Articles” list

- Follow Feed

• User A follows User B

• User B publishes a new article

• Article shows up in User A’s Your Feed

- **Additional coverage – pick any two** 
- [x] Edit / Delete Article

• Author can update body & tags, changes are visible

• Author can delete the article, it disappears from all lists

- [x] Favourite Toggle

• Logged-in user favourites / unfavourites an article

• Favourite counter updates accordingly

- [x] There must be a README with simple step-by-step instructions for running
the solution,
- [x] The solution must be able to run headless on Linux
- [x] All configuration must be parameterized (URL/domain, username, password,
etc)