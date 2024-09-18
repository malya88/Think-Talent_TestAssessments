from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome WebDriver
driver = webdriver.Chrome()  # or specify the path to your ChromeDriver

# Define the login URL and credentials
login_url = 'https://nextv3.thinktalent.info/login'  # Replace with the correct login endpoint
credentials = {
    'username': 'malyabanta88@gmail.com',  # Replace with your username
    'password': 'malya@123'  # Replace with your password
}


# Function to log into the application
def login(tab_index):
    driver.get(login_url)

    # Wait for username field to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))  # Adjust based on actual field name
    )

    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.NAME, 'password')  # Adjust based on actual field name

    username_field.send_keys(credentials['username'])
    password_field.send_keys(credentials['password'])

    # Submit the form
    password_field.submit()

    # Wait for login to complete and check for success
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//element_that_indicates_success"))  # Adjust as necessary
        )
        print(f"Login successful in tab {tab_index + 1}!")
    except Exception as e:
        print(f"Login failed in tab {tab_index + 1}: {str(e)}")


# Open multiple tabs and log in
for i in range(5):
    if i > 0:
        driver.execute_script("window.open('');")  # Open a new tab
        driver.switch_to.window(driver.window_handles[i])  # Switch to the new tab

    login(i)

# Keep the browser open for a while to view the results
driver.quit()  # Close the browser
