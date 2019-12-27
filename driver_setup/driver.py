from env_conf import base_url
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Driver(object):
    BASE_URL = base_url

    def __init__(self):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__driver.maximize_window()
        self.__driver.get(Driver.BASE_URL)

    def driver(self):
        return self.__driver
