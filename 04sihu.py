import requests
import re

url = "https://www.6886i.com/Html/63/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/67.0.3396.99 Safari/537.36"
}
response = requests.get(url, headers=headers)
r = response.content.decode()
ret = re.findall(r'<a href="(.*?)" target="_blank">', r)
url_list = []
for url in ret:
    url = "https://www.6886i.com"+url
    url_list.append(url)
print(url_list)

j = 1
for url in url_list:
    response = requests.get(url, headers=headers)
    # 使用正则表达式获取图片列表
    r = response.content.decode()
    imagelist = re.findall(r'<img src="(.*?)"/>', r)
    for i in imagelist:
        print(i)
        response = requests.get(i)
        with open('D:\python5\Reptilian\image\sihu\%d.jpg' % j, 'wb') as file:
            file.write(response.content)
        j += 1
        print(j)
