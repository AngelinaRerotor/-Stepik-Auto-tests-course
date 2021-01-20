from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    # link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num1 = int(num1.text)
    num2 = browser.find_element_by_id('num2')
    num2 = int(num2.text)
    sum = str(num1 + num2)
    print(sum)

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(sum)

    button = browser.find_element_by_tag_name('button').click()


    time.sleep(4)

finally:
    time.sleep(10)
    browser.quit()
