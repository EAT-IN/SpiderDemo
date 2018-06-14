import requests

# 创建session实例对象
session = requests.session()
post_url = "http://www.renren.com/PLogin.do"
post_data = {"email": "mr_mao_hacker@163.com", "password": "alarmchime"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/66.0.3359.181 Safari/537.36"
           }
# 使用session发送post请求,并把登陆后的cookie信息保存在session里面
r = session.post(post_url, data=post_data, headers=headers)
# 保存界面
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
