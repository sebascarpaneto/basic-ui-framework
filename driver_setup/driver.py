from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    BROWSER = 'Chrome'
    BASE_URL = 'http://www.aliexpress.com'

    @staticmethod
    def web_driver():
        if Driver.BROWSER == 'Chrome':
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            return 'Browser not supported'
        driver.maximize_window()
        driver.get(Driver.BASE_URL)
        return driver
