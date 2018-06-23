from selenium import webdriver
import time


class DouyuSpider(object):
    def __init__(self):
        # 开始链接
        self.start_url = "https://www.douyu.com/directory/all"
        # 实例化一个driver对象
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        # 同过定位获取所有ul标签下面的li标签的集合
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        # 定义一个空列表方便等下保存每一次遍历的字典数据
        content_list = []
        for li in li_list:
            item = {}
            item["room_img"] = li.find_element_by_xpath(".//span[@class='imgbox']/img").get_attribute("src")
            item["room_title"] = li.find_element_by_xpath("./a").get_attribute("title")
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            content_list.append(item)
        # 获取下一页的元素
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        for text in content_list:
            url = text["room_img"]
            title = text["room_title"]
            watch = text["watch_num"]
            text = "图片地址:{}  标题:{}  观看人数:{}\n".format(url, title, watch)
            with open("douyu.txt", "a", encoding="utf-8") as f:
                f.write(text)

    def run(self):
        self.driver.get(self.start_url)
        content_list, next_url = self.get_content_list()
        # 保存数据
        self.save_content_list(content_list)
        # 点击下一页元素，循环
        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list, next_url = self.get_content_list()
            self.save_content_list(content_list)


if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()
