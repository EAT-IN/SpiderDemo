import re
import requests

# 首先先访问目标网址
response = requests.get('https://www.douyu.com/directory/game/yz')
# 使用正则表达式获取图片列表
imagelist = re.findall(r'https://.*big.jpg', response.text)
j = 1
for i in imagelist:
    print(i)
    response = requests.get(i)
    with open('D:\python5\Reptilian\image\douyu\%d.jpg' % j, 'wb') as file:
        file.write(response.content)
    j += 1
    print(j)