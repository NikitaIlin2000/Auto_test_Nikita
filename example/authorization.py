from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.common.exceptions import NoSuchElementException
import time
import math

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('langust', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])

class TestAuthorization(): 

    def test_logpass(self,browser,langust):
        answer = math.log(int(time.time()))
        browser.get(langust)
        WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Войти"]'))
    ).click()
        browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('nikitka.ilin.1997@mail.ru')
        browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('2006105Qq')
        WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'[type="submit"]'))
    ).click()
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CLASS_NAME, 'no_such_light-tabs.ember-view')
            pytest.fail("Не должно быть модального окна")
        pole = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ember-text-area.ember-view.textarea.string-quiz__textarea')))
        pole.send_keys(answer)
        WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'submit-submission'))
    ).click()
        a = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(( By.CLASS_NAME,'smart-hints__hint')))
        assert 'Correct!' == a.text, f"Нужный текст для задания {a}"