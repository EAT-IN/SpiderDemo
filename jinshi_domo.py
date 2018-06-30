import requests
import re
import json

url = 'https://m.jin10.com/flash?maxId=20180629182139285100'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'}
response = requests.get(url, headers=headers)
r = response.content.decode()
html_str = json.loads(r)
for i in html_str:
    item = {}
    item["time"] = re.findall(r"(20\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", i)[0]
    item["content"] = re.findall(r".*?#.*?#20\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}#(.*?)#####.*?###.*?", i)[0]
    print(item)