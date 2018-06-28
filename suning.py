import requests
from lxml import etree

url = 'http://snbook.suning.com/web/trd-fl/999999/0.htm'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
response = requests.get(url, headers=headers)
r = response.content.decode()
html_str = etree.HTML(r)
li_list = html_str.xpath("//*[@id='mainSearch']/div[1]/ul/li")
for li in li_list:
    item = {}
    item["title"] = li.xpath("./div[2]/div[1]/a/text()")[0]
    item["content"] = li.xpath("./div[2]/div[3]/text()")[0]
    print(item)