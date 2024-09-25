import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@pytest.fixture(scope="function")
def setup_browser():
    # Setup: Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    yield driver
    # Teardown: Quit the browser after the test
    driver.quit()


def test_scenario_la(setup_browser):
    driver = setup_browser

    # List of users
    users = [
        {"username": "malyabanta88@gmail.com", "password": "malya@123"},
        {"username": "malyabanta88@gmail.com", "password": "malya@123"},
        {"username": "malyabanta88@gmail.com", "password": "malya@123"},
        {"username": "malyabanta88@gmail.com", "password": "malya@123"},
        {"username": "malyabanta88@gmail.com", "password": "malya@123"}
    ]

    for i, user in enumerate(users):
        # Open login page in a new tab for each user
        if i > 0:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[i])

        driver.get(
            "https://nextv3.thinktalent.info/oauth-service/oauth/authorize?response_type=code&client_id=next&scope=email&redirect_uri=https://nextv3.thinktalent.info/landing-user/login/user-authorized&USER_TYPE=USER")

        # Perform login
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(user["username"])
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(user["password"])
        driver.find_element(By.ID, "loginbtn").click()

        # Wait for the login to complete
        time.sleep(5)

        # Simulate navigating through the platform after login
        driver.find_element(By.CSS_SELECTOR,
                            "button.next_btn.next_btn.client_btn_font_size.test_all_account_access_btn_Malya.client.btn.btn-secondary").click()
        time.sleep(5)
        # driver.get("https://nextv3.thinktalent.info/landing-user/user/task-list")

        # Wait for the clickable image element and click
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next_img.img-fluid")))
        element.click()
        time.sleep(5)

        # Navigate to a specific page
        # driver.get("https://nextv3.thinktalent.info/vdc-user/user/batch-wizard/D34A3C827BDEFC40BC84BE32DB22A0A0")
        time.sleep(5)

        # Click dropdown toggle and log out
        driver.find_element(By.CSS_SELECTOR, "li.dropdown.nav-item > a.pro-pic.dropdown-toggle.nav-link").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,
                            "li.dropdown.nav-item > div.user-dd.dropdown-menu.dropdown-menu-right > a.dropdown-item").click()
        time.sleep(5)


def test_is_element_present(setup_browser):
    driver = setup_browser

    def is_element_present(how, what):
        try:
            driver.find_element(by=how, value=what)
            # Explicit wait to ensure the element is available
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((how, what)))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
    assert is_element_present(By.ID, "username") == True


def test_is_alert_present(setup_browser):
    driver = setup_browser

    def is_alert_present():
        try:
            driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    assert is_alert_present() == False


def test_close_alert_and_get_its_text(setup_browser):
    driver = setup_browser
    accept_next_alert = True

    def close_alert_and_get_its_text():
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            if accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            accept_next_alert = True

    # Assuming an alert will appear; otherwise, skip this in actual testing
    # assert close_alert_and_get_its_text() == "Expected alert text"
