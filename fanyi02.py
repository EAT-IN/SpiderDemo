import requests
import json


class FanyiSpider(object):
    def __init__(self, query_string):
        self.query_string = query_string
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
                        }

    def languge_type(self):
        post_data = {
            "query": self.query_string
        }
        post_url = "http://fanyi.baidu.com/langdetect"
        r = requests.post(post_url, data=post_data, headers=self.headers)
        dict_ret = json.loads(r.content.decode())
        language = dict_ret["lan"]
        return language

    def run(self):
        language = self.languge_type()
        if language == "zh":
            from_lan = "zh"
            to_lan = "en"
        else:
            from_lan = "en"
            to_lan = "zh"
        post_data = {
            "query": self.query_string,
            "from": from_lan,
            "to": to_lan,
        }
        post_url = "http://fanyi.baidu.com/basetrans"
        r = requests.post(post_url, data=post_data, headers=self.headers)
        dict_ret = json.loads(r.content.decode())
        ret = dict_ret["trans"][0]["dst"]
        print(ret)


if __name__ == "__main__":
    query_string = input("请输入你要查询的词汇:")
    fanyispider = FanyiSpider(query_string)
    fanyispider.run()
