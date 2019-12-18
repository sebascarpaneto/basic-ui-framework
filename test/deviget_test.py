import pytest
from assertpy import assert_that
from driver_setup.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from ali_express_page_objects.landing_page import close_pop_up, search_box, search

web_driver = Driver().driver()


@pytest.mark.test
def ali_test():
    web_driver.find_element(By.XPATH, '/html/body/div[5]/div/div/a').click()
    web_driver.find_element(By.ID, 'search-key').click()
    web_driver.find_element(By.XPATH, '//*[@id="form-searchbar"]/div[1]/input').send_keys('Iphone')
    web_driver.quit()


ali_test()
