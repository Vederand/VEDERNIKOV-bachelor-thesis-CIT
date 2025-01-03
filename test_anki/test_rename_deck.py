import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.login_anki_profile import login_anki_profile

# new name of a target deck, expected result
test_data = (("3333","change"),
             ("","warning"),
             ("2222","warning"))

@pytest.mark.parametrize("new_name, result", test_data)
def test_rename_deck(new_name, result):

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    target_deck = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"(//button[@type='button'][normalize-space()='Actions'])[1]")))
    target_deck.click()
    rename = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@class='dropdown-menu show']//button[@type='button'][normalize-space()='Rename']")))
    rename.click()

    # working with an alert for deck renaming
    rename_deck_alert = driver.switch_to.alert
    rename_deck_alert.send_keys(new_name)
    rename_deck_alert.accept()

    # asserting the expected results
    if(result=="change"):
        assert driver.find_element(By.XPATH,f"//*[text()='{new_name}']")
    else:
        assert driver.find_element(By.XPATH, "//*[text()='Warning']")

    driver.quit()