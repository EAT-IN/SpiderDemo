import requests
import re

url = "https://m.ybdu.com/xiaoshuo/9/9732/1906713.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36",
    "Referer": "https://www.ybdu.com/xiaoshuo/9/9732/1906713.html",
}
response = requests.get(url, headers=headers)
r = response.text  # 获取html字符串
ret = re.findall(r'<div class="txt" id="txt">([\s\S]*?)</div>', r)
ret = ret[0]
content = re.sub(r"<br />|&nbsp;", "", ret)
print(content)
