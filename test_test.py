from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
base_url = 'http://www.aliexpress.com'
driver.get(base_url)
driver.implicitly_wait(10)
# Close pop up
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/a'))).click()
# driver.find_element_by_xpath('/html/body/div[5]/div/div/a').click()
# Input Iphone on searchbox
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'search-key'))).send_keys('Iphone')
# driver.find_element_by_id('search-key').send_keys('Iphone')
# Click on Search
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="form-searchbar"]/div[1]/input'))).click()
# driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()
driver.implicitly_wait(10)
# Close pop up
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/a'))).click()
# driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/a').click()
# Click on next page
# driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/button[2]').click()
# driver.implicitly_wait(20)
# Click on second item
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li[2]/div/div[1]/a/img'))).click()
# driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li[2]/div/div[1]/a/img').click()
driver.implicitly_wait(10)
# Switch to new tab
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'body'))).send_keys(Keys.CONTROL + Keys.TAB)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.implicitly_wait(10)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[11]/span[1]/button'))).click()
# driver.quit()
