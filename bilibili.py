import requests
from lxml import etree

url = "https://api.bilibili.com/x/v1/dm/list.so?oid=42862145"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.87 Safari/537.36"
}
response = requests.get(url, headers=headers)
r = response.content.decode()
html_str = etree.HTML(r.encode())
p_list = html_str.xpath("//d/text()")
for p in p_list:
    content = (p + "\n")
    with open("bilibili.txt", "a", encoding="utf-8") as f:
        f.write(content)
