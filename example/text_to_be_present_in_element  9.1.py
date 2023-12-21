from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    money = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[style="display:inline;float:right"]'), "$100")
    ) # явное ожидание по тексту "$100"
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="book"]'))
    ).click()
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    x = browser.find_element(By.CSS_SELECTOR, 'body > form > div > div > div > label > span:nth-child(2)').text
    y = calc(x)
    browser.find_element(By.CLASS_NAME, 'form-control').send_keys(y)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Submit"]'))
    ).click() 

finally:
    time.sleep(5)
    browser.quit()