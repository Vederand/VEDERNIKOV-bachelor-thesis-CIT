import time

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.get_data_fromExcel import get_data_fromEXEL
from utilities.login_anki_profile import login_anki_profile

# test_data[0] my rows
# test_data[1] my dict
# test_data[2] final result
test_data = get_data_fromEXEL(
    "C:\\Users\\Andrew\\PythonForSelenium\\anki_web\\excel_files\\search.xlsx")

@pytest.mark.parametrize("deck_name, tag, front, card_type",test_data[0])
def test_search(deck_name, tag, front, card_type):

    # building a prompt text using available input parameters
    prompt = ""
    if(deck_name!="empty"):
        prompt += f"deck:{test_data[1][deck_name]} "
    if(tag!="empty"):
        prompt += f"tag:{test_data[1][tag]} "
    if(front!="empty"):
        prompt += f"front:{test_data[1][front]} "
    if(card_type!="empty"):
        prompt += f"note:{test_data[1][card_type]}"

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    # performing searching actions
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[.='Search']"))).click()
    search_input_field = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input")))
    search_input_field.clear()
    search_input_field.send_keys(prompt)

    search_button = driver.find_element(By.XPATH,"//button[.='Search']")
    search_button.click()

    time.sleep(2)

    # asserting the expected results
    assert driver.find_element(By.XPATH,f"//*[text()='1a / 2abc']")

    driver.quit()

