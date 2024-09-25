# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time


class TestSuiteTwo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_suite_two(self):
        driver = self.driver
        # Loop to perform 5 login iterations
        for i in range(5):
            print(f"Iteration {i + 1} of login:")
            driver.get(
                "https://nextv3.thinktalent.info/oauth-service/oauth/authorize?response_type=code&client_id=next&scope=email&redirect_uri=https://nextv3.thinktalent.info/landing-user/login/user-authorized&USER_TYPE=USER")
            driver.find_element(By.ID, "password").click()
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys("malyabanta88@gmail.com")
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys("malya@123")
            driver.find_element(By.ID, "loginbtn").click()

            time.sleep(2)  # Wait for the page to load

            # Navigate to other pages or perform further actions
            driver.get("https://nextv3.thinktalent.info/landing-user/notification/all-accounts")
            driver.find_element(By.CSS_SELECTOR("button[type='submit']").click()
            driver.get("https://nextv3.thinktalent.info/landing-user/user/task-list")

            # Perform logout at the end of each iteration
            driver.get("https://nextv3.thinktalent.info/oauth-service/logout")

            print(f"Iteration {i + 1} completed")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
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
