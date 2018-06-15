import requests
import json
import time

while True:
    print("------欢迎使用翻译小程序(双击回车退出)------")
    query_string = input("请输入你要查询的词汇:")

    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
               }
    post_data = {
        "query": query_string
    }
    post_url = "http://fanyi.baidu.com/langdetect"
    r = requests.post(post_url, data=post_data, headers=headers)
    dict_ret = json.loads(r.content.decode())
    try:
        language = dict_ret["lan"]
    except Exception as f:
        print("------感谢您的使用,再见!------")
        time.sleep(1.5)
        break

    if language == "zh":
        from_lan = "zh"
        to_lan = "en"
    else:
        from_lan = "en"
        to_lan = "zh"

    post_data = {
        "query": query_string,
        "from": from_lan,
        "to": to_lan,
    }
    post_url = "http://fanyi.baidu.com/basetrans"
    r = requests.post(post_url, data=post_data, headers=headers)
    dict_ret = json.loads(r.content.decode())
    ret = dict_ret["trans"][0]["dst"]
    print("翻译的结果为:" + ret)
    print("")
