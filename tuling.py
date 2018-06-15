import requests
import json

print("------欢迎进入图灵机器人聊天系统------")
while True:
    msg = input("我:")
    url = "http://www.tuling123.com/openapi/api"
    data = {"key": "c8c37b30b7654db78f1d088ae9393172", "info": msg}
    r = requests.post(url, data=data)
    dict = json.loads(r.content.decode())
    ret = dict['text']
    print("萌萌:%s" % ret)
