import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.login_anki_profile import login_anki_profile

# name of the target deck, expected message
test_data = (("1111","Show Answer"),
             ("2222","Congratulations! You have finished this deck for now."))

@pytest.mark.parametrize("deck_name, result",test_data)
def test_start_session(deck_name, result):

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    target_deck = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,f"//*[text()='{deck_name}']")))
    target_deck.click()

    # asserting the expected results
    assert wait.until(expected_conditions.presence_of_element_located((By.XPATH,f"//*[text()='{result}']")))

    driver.quit()