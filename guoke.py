import requests
import re

url = "https://www.guokr.com/ask/highlight/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.87 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_str = response.content.decode()
# ret = re.findall(r'<h2><a target="_blank"(.*)</a></h2>', html_str)
# # print(ret)
# for i in ret:
#     temp = i.split(">")
#     print(temp[1]+"\n")
ret = re.findall(r'<h2><a target="_blank" href=".*">(.*)</a></h2>', html_str)
for i in ret:
    print(i+"\n")