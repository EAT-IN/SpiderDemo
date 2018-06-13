import requests

response = requests.get("http://www.sina.com")
# print(response.request.headers)
print(response.content.decode())
