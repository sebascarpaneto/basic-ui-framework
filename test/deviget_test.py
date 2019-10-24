import pytest
from assertpy import assert_that
from driver_setup.driver import Driver
from ali_express_page_objects.landing_page import close_pop_up, search_box, search, By
from ali_express_page_objects.first_page import close_second_pop_up, next_page_button
from ali_express_page_objects.second_page import second_item
from ali_express_page_objects.item_page import quantity_element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = Driver.web_driver()
switch_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'body'))).send_keys(
    Keys.CONTROL + Keys.TAB)


@pytest.mark.deviget
def ali_test():
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(close_pop_up)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(search_box)).send_keys('Iphone')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(search)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(close_second_pop_up)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(next_page_button)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(second_item)).click()
    switch_tab()
    quantity = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(quantity_element)).text()
    assert_that(quantity, 1)
    driver.quit()


ali_test()
