# -*- coding: utf-8 -*-
import re
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Case1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case1(self):
        driver = self.driver
        driver.get("https://nextv3.thinktalent.info/oauth-service/oauth/authorize?response_type=code&client_id=next"
                   "&scope=email&redirect_uri=https://nextv3.thinktalent.info/landing-user/login/user-authorized"
                   "&USER_TYPE=USER")
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys("malyabanta88@gmail.com")
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("malya@123")
        driver.find_element(By.ID, "loginbtn").click()
        time.sleep(5)

        # driver.get("https://nextv3.thinktalent.info/landing-user/login/user-authorized?code"
        #            "=8B2wB7lZu0KqxTfJErnNaWszBouquetR")
        # driver.get("https://nextv3.thinktalent.info/landing-user/notification/all-accounts")
        # driver.find_element(By.CSS_SELECTOR, "button.next_btn.next_btn.client_btn_font_size"
        #                                      ".test_all_account_access_btn_Malya.client.btn.btn-secondary").click()
        # time.sleep(5)
        # driver.get("https://nextv3.thinktalent.info/landing-user/user/task-list")
        # driver.find_element(By.CSS_SELECTOR, ".next_img.img-fluid").click()
        # time.sleep(5)
        # driver.get("https://nextv3.thinktalent.info/vdc-user/user/batch-wizard/D34A3C827BDEFC40BC84BE32DB22A0A0")
        # driver.find_element(By.CSS_SELECTOR, ".user-dd.dropdown-menu.dropdown-menu-right.show").click()
        # time.sleep(5)
        # driver.find_element(BY.LINK_TEXT, "Logout").click()
        # time.sleep(10)
        # driver.get("https://nextv3.thinktalent.info/oauth-service/logout")
        # driver.get("https://nextv3.thinktalent.info/oauth-service/oauth/authorize?response_type=code&client_id=next"
        #            "&scope=email&redirect_uri=https://nextv3.thinktalent.info/landing-user/login/user-authorized"
        #            "&USER_TYPE=USER")

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
