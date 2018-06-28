from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.jin10.com/")
list = driver.find_elements_by_xpath("//div[@class='jin-flash_wrap J_flash_wrap']/div")
content = []
for i in list:
    item = {}
    item["title"] = i.find_element_by_xpath(".//p").text
    print(item["title"]+"\n")
