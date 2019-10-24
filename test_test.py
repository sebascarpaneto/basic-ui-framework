from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
base_url = 'http://www.aliexpress.com'
driver.get(base_url)
driver.implicitly_wait(20)
# Close pop up
driver.find_element_by_xpath('/html/body/div[5]/div/div/a').click()
# Input Iphone on searchbox
driver.find_element_by_id('search-key').send_keys('Iphone')
# Click on Search
driver.find_element_by_xpath('//*[@id="form-searchbar"]/div[1]/input').click()
driver.implicitly_wait(20)
# Close pop up
driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/a').click()
# Click on next page
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[3]/div/div[1]/div/button[2]').click()
driver.implicitly_wait(20)
# Click on second item
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/li[2]/div/div[1]/a/img').click()
driver.implicitly_wait(20)
# Switch to new tab
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
driver.quit()


