# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re


class ScenarioLatest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_scenario_la(self, BY=None):
        driver = self.driver

        # List of 5 users
        users = [
            {"username": "malyabanta88@gmail.com", "password": "malya@123"},
            {"username": "malyabanta88@gmail.com", "password": "malya@123"},
            {"username": "malyabanta88@gmail.com", "password": "malya@123"},
            {"username": "malyabanta88@gmail.com", "password": "malya@123"},
            {"username": "malyabanta88@gmail.com", "password": "malya@123"}
        ]

        for i, user in enumerate(users):
            # Open the login page in a new tab
            if i > 0:  # For subsequent users, open a new tab
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[i])

            # Navigate to the login page
            driver.get(
                "https://nextv3.thinktalent.info/oauth-service/oauth/authorize?response_type=code&client_id=next&scope=email&redirect_uri=https://nextv3.thinktalent.info/landing-user/login/user-authorized&USER_TYPE=USER")

            # Perform login for each user
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys(user["username"])
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(user["password"])
            driver.find_element(By.ID, "loginbtn").click()

            # Wait for some time to allow login to complete
            time.sleep(5)

            # Simulate navigating through the platform after login
            driver.get(
                "https://nextv3.thinktalent.info/landing-user/login/user-authorized?code=zWluw1oxdgnZuxJNNfvt1EejFTSRQw")
            driver.get("https://nextv3.thinktalent.info/landing-user/notification/all-accounts")
            driver.find_element(By.CSS_SELECTOR, "button.next_btn.next_btn.client_btn_font_size"
                                                 ".test_all_account_access_btn_Malya.client.btn.btn-secondary").click()
            time.sleep(5)
            driver.get("https://nextv3.thinktalent.info/landing-user/user/task-list")
            element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next_img.img-fluid")))
            element.click()
            time.sleep(5)

            # Navigate to a specific page after clicking an image
            driver.get("https://nextv3.thinktalent.info/vdc-user/user/batch-wizard/D34A3C827BDEFC40BC84BE32DB22A0A0")
            time.sleep(5)

            # Click the dropdown toggle to open the dropdown menu
            driver.find_element(By.CSS_SELECTOR, "li.dropdown.nav-item > a.pro-pic.dropdown-toggle.nav-link").click()
            time.sleep(5)

            # Click the Logout link from the dropdown menu
            driver.find_element(By.CSS_SELECTOR,
                                "li.dropdown.nav-item > div.user-dd.dropdown-menu.dropdown-menu-right > a.dropdown-item").click()
            time.sleep(5)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
