import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link):
    link = f"http://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    browser.implicitly_wait(6)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name('textarea').send_keys(answer)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()
    check_text = browser.find_element_by_class_name("smart-hints__hint").text
    print(check_text)

    assert 'Correct!' == check_text, "NOT CORRECT"
