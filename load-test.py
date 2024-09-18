

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # or specify the path to your ChromeDriver

# Define the login URL and credentials
login_url = 'https://nextv3.thinktalent.info/landing-user/'  # Replace with the correct login endpoint
credentials = {
    'username': 'malyabanta88@gmail.com',  # Replace with your username
    'password': 'malya@123'     # Replace with your password
}

# Function to log into the application
def login(tab_index):
    driver.get(login_url)
    time.sleep(2)  # Wait for the page to load (adjust as necessary)

    # Find the username and password fields and log in
    username_field = driver.find_element(By.NAME, 'username')  # Adjust based on actual field name
    password_field = driver.find_element(By.NAME, 'password')  # Adjust based on actual field name

    username_field.send_keys(credentials['username'])
    password_field.send_keys(credentials['password'])

    # Submit the form
    password_field.submit()
    time.sleep(2)  # Wait for login to process (adjust as necessary)

    # Check for successful login (you may need to adjust this condition)
    if 'Welcome' in driver.page_source:  # Change this based on actual content
        print(f"Login successful in tab {tab_index + 1}!")
    else:
        print(f"Login failed in tab {tab_index + 1}.")

# Open multiple tabs and log in
for i in range(5):
    if i > 0:
        driver.execute_script("window.open('');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[i])  # Switch to the new tab

    login(i)

# Keep the browser open for a while to view the results
time.sleep(10)  # Adjust this duration as needed
driver.quit()  # Close the browser
