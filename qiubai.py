import re
import requests

url = "https://www.qiushibaike.com/text/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.87 Safari/537.36"
}
response = requests.get(url, headers=headers)
r = response.content.decode()
# print(type(r))
context = re.findall(r'<div class="content">([\s\S]*?)</div>', r)
for i in context:
    i = re.sub(r"\n|<span>|</span>|<br/>", "", i)
    print(i+"\n")