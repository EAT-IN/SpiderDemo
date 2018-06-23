from selenium import webdriver


class Money(object):
    def __init__(self):
        # 先给一个开始的url链接
        self.url = "http://fund.eastmoney.com/data/fundranking.html"
        # 创建实例化对象
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        # 获取到每一个tr标签的集合
        tr_list = self.driver.find_elements_by_xpath("//table[@id='dbtable']/tbody/tr")
        # 定义一个列表用来接收所有的数据进行保存
        content_list = []
        for tr in tr_list:
            item = {}
            item["num"] = tr.find_element_by_xpath("./td[2]").text
            item["core"] = tr.find_element_by_xpath("./td[3]/a").text
            item["name"] = tr.find_element_by_xpath("./td[4]/a").text
            item["plus"] = tr.find_element_by_xpath("./td[9]").text
            content_list.append(item)

        return content_list

    def save_content_list(self, content_list):
        for text in content_list:
            num = text["num"]
            core = text["core"]
            name = text["name"]
            plus = text["plus"]
            content= "序号:{}  基金代码:{}  基金简称:{}  日增长率:{}\n".format(num, core, name, plus)
            with open("money.txt", "a", encoding="utf-8") as f:
                f.write(content)
        self.driver.quit()

    def run(self):
        # 发送请求获取响应
        self.driver.get(self.url)
        # 获取数据
        content_list = self.get_content_list()
        # 保存数据
        self.save_content_list(content_list)


if __name__ == "__main__":
    money = Money()
    money.run()
