from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("button")
    input1.click()
    redirect_page = browser.window_handles[1] # определяем нужную вкладку
    browser.switch_to.window(redirect_page) # переключаемся на выбранную вкладку


    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_tag_name('button')
    button.click()

    time.sleep(2)

finally:
    time.sleep(10)
    browser.quit()
