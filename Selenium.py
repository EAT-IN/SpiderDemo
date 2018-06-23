from selenium import webdriver
import time

driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com")
driver.save_screenshot("./baidu.png")
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()

# print(driver.page_source)
# cookies = driver.get_cookies()
# cookies = {i["name"]: ["value"] for i in cookies}
# print(cookies)


time.sleep(5)
driver.quit()