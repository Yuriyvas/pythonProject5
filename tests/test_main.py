import allure
import time
from allure_commons.types import AttachmentType
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
firefox_options.set_headless()
driver = webdriver.Firefox(options=firefox_options)

class TestPageSearch:
    def setup(self):
        self.driver = driver
    def teardown(self):
        self.driver.quit()

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "google.com"')
    def test_google_search(self):
        self.driver.get('https://google.com')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "yandex.ru"')
    def test_yandex_search(self):
        self.driver.get('https://yandex.ru')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title =='Яндекс'

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "mail.ru"')
    def test_mail_search(self):
        self.driver.get('https://mail.ru')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title =='Mail.ru'

