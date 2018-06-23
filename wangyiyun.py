import requests
from lxml import etree


class Music(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/67.0.3396.87 Safari/537.36"}

    def run(self):
        response = requests.get(self.url, headers=self.headers)
        r = response.content.decode()
        html_str = etree.HTML(r)
        content_list = html_str.xpath("//ul[@id='m-pl-container']/li")
        for content in content_list:
            item = {}
            item["img"] = content.xpath("./div/img/@src")
            item["title"] = content.xpath("./div/a/@title")
            item["author"] = content.xpath("./p[2]/a/@title")
            print(item)


if __name__ == "__main__":
    temp_url = "https://music.163.com/#/discover/playlist/?order=hot&cat=%E8%AF%B4%E5%94%B1&limit=35&offset={}"
    url_list = [temp_url.format(i*35) for i in range(30)]
    for url in url_list:
        music = Music(url)
        music.run()

# from selenium import webdriver
# import time
#
#
# class Music(object):
#     def __init__(self):
#         self.url = "https://music.163.com/#/discover/playlist/?cat=说唱"
#         self.driver = webdriver.Chrome()
#
#     def get_content_list(self):
#         # 获取所有的li标签
#         li_list = self.driver.find_elements_by_xpath("//ul[@id='m-pl-container']/li")
#         content_list = []
#         for li in li_list:
#             item = {}
#             item["img"] = li.find_element_by_xpath("./div/img").get_attribute("src")
#             item["title"] = li.find_element_by_xpath("./div/a").get_attribute("title")
#             item["author"] = li.find_element_by_xpath("./p[2]/a").get_attribute("title")
#             print(item)
#         time.sleep(3)
#         self.driver.quit()
#
#     def run(self):
#         self.driver.get(self.url)
#         self.get_content_list()
#
#
# if __name__ == "__main__":
#     music = Music()
#     music.run()
