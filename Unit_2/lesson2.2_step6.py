from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    click1 = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    click1.click()
    click2 = browser.find_element_by_css_selector('[for="robotsRule"]')
    click2.click()

    button.click()

finally:
    time.sleep(10)
    browser.quit()
