import requests

url = "https://d1.xia12345.com/d/62/2018/07/8tdajRHK.mp4"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
response = requests.get(url, headers=headers)
r = response.content
with open("oumei.mp4", "wb") as f:
    f.write(r)