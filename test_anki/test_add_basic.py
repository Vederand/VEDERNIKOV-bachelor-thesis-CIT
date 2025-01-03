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
    "C:\\Users\\Andrew\\PythonForSelenium\\anki_web\\excel_files\\add_basic.xlsx")

@pytest.mark.parametrize("front, back, result",test_data[0])
def test_add_basic(front, back, result):

    # driver setup and login tasks
    driver = login_anki_profile()

    wait = WebDriverWait(driver, 5)

    add = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[.='Add']")))
    add.click()

    # filling in the required fields
    front_field = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "(//div[@class='form-control field'])[1]")))
    back_field = wait.until(
        expected_conditions.element_to_be_clickable((By.XPATH, "(//div[@class='form-control field'])[2]")))
    front_field.send_keys(test_data[1][front])
    back_field.send_keys(test_data[1][back])

    # asserting the expected results
    if result == "added":
        add_button = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[.='Add']")))
        add_button.click()
        assert wait.until(expected_conditions.visibility_of_element_located((By.XPATH, f"//*[text()={test_data[2]}]")))
    else:
        assert wait.until(
            expected_conditions.invisibility_of_element_located((By.XPATH, f"//*[text()={test_data[2]}]")))

    driver.quit()
