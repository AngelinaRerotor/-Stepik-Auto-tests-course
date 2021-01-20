from selenium import webdriver
import unittest
import time


class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Unsuccessful registration")

    def test_registration_2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("Smolensk@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Unsuccessful registration")


if __name__ == "__main__":
    unittest.main()
