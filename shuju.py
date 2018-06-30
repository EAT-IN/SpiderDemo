from pprint import pprint

import time
import requests
import json
import re

a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
b = time.strftime("%H:%M:%S")
start_time = a+" "+b
url = "https://view.jin10.com/flash?&max_time={}".format(start_time)

while True:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/67.0.3396.87 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    r = response.content.decode()
    ret = re.findall(r'\{.*\}', r)
    # 注意的是这里的字典是字符串 json的字符串  还不是python类型 就要进行转化
    html_content= json.loads(ret[0])
    # print(type(html_content))  # 打印类型进行验证
    content_list= (html_content["data"])
    for content in content_list:
        print(content["time_show"]+content["title_content"]+"\n")
        # print(content)
    time = content_list[-1]
    last_time = time["time_show"]
    print(last_time)
    url = "https://view.jin10.com/flash?&max_time={}".format(last_time)
