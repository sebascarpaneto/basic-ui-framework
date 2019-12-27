import pytest
from assertpy import assert_that
from driver_setup.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.example_page import close_pop_up, search_box, search

web_driver = Driver().driver()


# select = Select(driver.find_element_by_id('fruits01'))
# select.select_by_visible_text('Banana')
# select.select_by_value('1')

@pytest.mark.test
def ali_test():
    web_driver.find_element(By.XPATH, close_pop_up).click()
    web_driver.find_element(By.ID, search_box).click()
    web_driver.find_element(By.XPATH, search).send_keys('Iphone')
    web_driver.quit()


ali_test()
