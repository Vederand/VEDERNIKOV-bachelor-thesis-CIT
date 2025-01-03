from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from selenium import webdriver


def login_anki_profile():
    """
    method for performing login into a target "ankiweb" account.

    Returns:
        driver (Chrome driver object): a setup Chrome driver object with performed login tasks.

    """

    # setting up a Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ankiweb.net/account/login")

    wait = WebDriverWait(driver, 5)

    # performing log in tasks
    password_field = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']")))
    email_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    email_field.send_keys("your_username")
    password_field.send_keys("your_password")

    login_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[.='Log In']")))
    login_button.click()

    return driver