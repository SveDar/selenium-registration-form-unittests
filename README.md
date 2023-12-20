# Selenium Registration Form Tests

This repository contains Selenium tests for a registration form using Python and the unittest framework.

## Prerequisites

- Python 3.x installed
- Chrome browser installed
- ChromeDriver executable downloaded and its path updated in the Python scripts

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/selenium-registration-form-tests.git
Navigate to the project directory:
cd selenium-registration-form-tests

Install the required Selenium package:
pip install selenium

## Files
1. login.html
The login.html file represents a simple login form with username, password, and a submit button. It includes client-side validation using JavaScript.

2. fail_testregistrationform.py
The fail_testregistrationform.py script contains a Selenium test case (FailTestRegistrationForm) that intentionally fails by submitting an empty first name. This is to demonstrate a failing scenario.

3. pass_testregistrationcode.py
The pass_testregistrationcode.py script contains a Selenium test case (PassTestRegistrationForm) that successfully submits valid data to the registration form. This is to demonstrate a passing scenario.

4. test_runner.py
The test_runner.py script is a test runner that orchestrates the execution of the tests. It includes both the failing and passing test cases.

## Running Tests
To execute the tests, follow these steps:

Ensure that the Chrome browser is installed on your system.

Download ChromeDriver from the official ChromeDriver website: https://sites.google.com/chromium.org/driver/

Update the paths to the ChromeDriver executable in the following files:

fail_testregistrationform.py
pass_testregistrationcode.py
test_runner.py
Open a terminal and navigate to the project directory:


cd selenium-registration-form-tests
Run the test runner:


python test_runner.py
This will execute both the failing and passing test cases.

View the test results in the terminal. If all tests pass, you'll see "All tests passed!".

Feel free to explore and modify the scripts as needed for your specific use case.





