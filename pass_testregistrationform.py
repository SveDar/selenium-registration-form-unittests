import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PassTestRegistrationForm(unittest.TestCase):
    def setUp(self):
        # Set the path to your webdriver (e.g., chromedriver.exe)
        self.webdriver_path = 'C:\TU\pis\chromedriver_win32\chromdriver.exe'
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Open the registration form page
        self.driver.get('C:\TU\pis\login-page-main\login-page-main\login.html')

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_registration_form_submission(self):
        # Find form fields by ID
        first_name_input = self.driver.find_element(By.ID, 'firstname')
        last_name_input = self.driver.find_element(By.ID, 'lastname')
        email_input = self.driver.find_element(By.ID, 'email')
        submit_button = self.driver.find_element(By.TAG_NAME, 'button')

        # Fill in the form fields
        first_name_input.send_keys('John')
        time.sleep(1)
        last_name_input.send_keys('Doe')
        time.sleep(1)
        email_input.send_keys('john.doe@example.com')
        time.sleep(1)

        # Click the submit button
        submit_button.click()
        time.sleep(1)

        # Wait for the "Thank You" container to be visible
        try:
            thank_you_container = WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.ID, 'thankYouContainer'))
            )
            self.assertTrue(thank_you_container.is_displayed(), "Thank You container is visible!")
        except Exception as e:
            self.fail(f"Thank You container is not visible. Exception: {e}")

if __name__ == '__main__':
    unittest.main()
