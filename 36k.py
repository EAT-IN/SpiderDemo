import requests
import re

url = "http://36kr.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.87 Safari/537.36"
}
response = requests.get(url, headers=headers)

html_str = response.content.decode()

ret = re.findall(r"<h3 data-stat(.*)</h3>", html_str)
print(ret)