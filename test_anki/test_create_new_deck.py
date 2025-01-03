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
    "C:\\Users\\Andrew\\PythonForSelenium\\anki_web\\excel_files\\create_deck.xlsx")

@pytest.mark.parametrize("name, result",test_data[0])
def test_create_new_deck(name, result):

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    create_deck = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[.='Create Deck']")))
    create_deck.click()

    # working with an alert for deck creation
    add_deck_alert = driver.switch_to.alert
    add_deck_alert.send_keys(test_data[1][name])
    add_deck_alert.accept()

    # asserting the expected results
    if result == "add":
        assert wait.until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//button[text()='{test_data[1][name]}']")))
    else:
        assert wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, f"//*[text()='{test_data[2]}']")))

    driver.quit()
