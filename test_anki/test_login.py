import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.get_data_fromExcel import get_data_fromEXEL
from selenium import webdriver

# test_data[0] my rows
# test_data[1] my dict
# test_data[2] final result
test_data = get_data_fromEXEL("C:\\Users\\Andrew\\PythonForSelenium\\anki_web\\excel_files\\login.xlsx")

@pytest.mark.parametrize("email ,password, result",test_data[0])
def test_login(email, password, result):

    # setting up a Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ankiweb.net/account/login")

    wait = WebDriverWait(driver,5)

    # performing login tasks
    password_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@autocomplete='current-password']")))
    email_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
    email_field.send_keys(test_data[1][email])
    password_field.send_keys(test_data[1][password])

    # asserting the expected results
    if result == "login":
        login_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[.='Log In']")))
        login_button.click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[.='Log Out']")))
        assert driver.current_url == test_data[2]

    else:
        assert driver.current_url != test_data[2]

    driver.quit()