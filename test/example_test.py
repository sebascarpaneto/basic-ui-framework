import pytest
import re
from selenium.common.exceptions import TimeoutException
from driver_setup.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import close_pop_up_button_1, close_pop_up_button_2, close_pop_up_button_3, search_box, search, \
    sign_in, log_in_frame, input_email, input_password, log_in_button, item, item_availability

web_driver = Driver().driver()


def close_alert(close_button_locator):
    try:
        WebDriverWait(web_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, close_button_locator))).click()
    except TimeoutException:
        pass


@pytest.mark.test
def ali_test():
    close_alert(close_pop_up_button_1)
    web_driver.find_element(By.XPATH, sign_in).click()
    web_driver.switch_to.frame(log_in_frame)
    web_driver.find_element(By.XPATH, input_email).send_keys('scarpaneto@zenfolio.com')
    web_driver.find_element(By.XPATH, input_password).send_keys('asd456')
    web_driver.find_element(By.XPATH, log_in_button).click()
    web_driver.switch_to.default_content()
    close_alert(close_pop_up_button_1)
    web_driver.find_element(By.ID, search_box).send_keys('Iphone')
    web_driver.find_element(By.XPATH, search).click()
    close_alert(close_pop_up_button_2)
    web_driver.find_element(By.XPATH, item).click()
    close_alert(close_pop_up_button_3)
    web_driver.switch_to.window(web_driver.window_handles[1])
    availability = web_driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[8]/div[2]/div').text
    stock_number = float(re.sub(r'[a-z]+', '', availability, re.I))
    assert stock_number > 0
    print(availability)
    web_driver.quit()


ali_test()
