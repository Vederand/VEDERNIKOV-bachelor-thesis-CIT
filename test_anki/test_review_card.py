import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.login_anki_profile import login_anki_profile

# deck name location of the card, action
test_data = (("1111","Again"),
             ("1111","Hard"),
             ("1111","Good"),
             ("1111","Easy"))

@pytest.mark.parametrize("deck_name, action",test_data)
def test_review_card(deck_name, action):

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    # choosing a deck, pressing "show answer", choosing the action
    target_deck = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[text()='{deck_name}']")))
    target_deck.click()
    show_answer = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='Show Answer']")))
    show_answer.click()
    action_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f"//*[text()='{action}']")))
    action_button.click()

    # asserting the expected results
    assert wait.until(expected_conditions.invisibility_of_element_located((By.XPATH,f"//*[text()='{action}']")))

    driver.quit()