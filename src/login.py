from dotenv import dotenv_values
import os
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def saveCookies(driver):
    # Get and store cookies after login
    cookies = driver.get_cookies()

    # Store cookies in a file
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)
    print('New Cookies saved successfully')


def loadCookies(driver):
    # Check if cookies file exists
    if 'cookies.json' in os.listdir():

        # Load cookies to a vaiable from a file
        driver.get('https://twitter.com')
        with open('cookies.json', 'r') as file:
            cookies = json.load(file)

        # Set stored cookies to maintain the session
        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        print('No cookies file found')
        USER_NAME = input('USER_NAME: ')
        PASSWORD = input('PASSWORD : ')
        login(driver,USER_NAME,PASSWORD)# Login to Twitter
        saveCookies(driver) # Save cookies
    
    driver.refresh() # Refresh Browser after login

# Initialize the WebDriver
def login(driver,USER_NAME,PASSWORD):
    
    driver.get("https://twitter.com/login")
    driver.implicitly_wait(10)
    
    # Find the username/email and password input fields
    # Enter Twitter username/email and password from environment variables
    username_field = driver.find_element(By.XPATH,'//input[@name="text"]')
    username_field.send_keys(USER_NAME)
    username_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(10) 
    password_field = driver.find_element(By.XPATH,'//input[@name="password"]')
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)

    