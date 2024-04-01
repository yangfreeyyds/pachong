import json
import requests
from lxml import etree
from login_crypto import encrypto
from python_js_encrypto import js_encrypto


users = [
    {"username":"demo123", "password":"demo123"},
    {"username":"demo1234", "password":"demo1234"},
    {"username":"test1234", "password":"test1234"},
    {"username":"test123", "password":"test123"},
]

def main(username, password):
    url = 'http://shanzhi.spbeen.com/login/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Cookie": "csrftoken=5H9PDQ6TAxknuydbn6IVhmZfGmGwsC6hT1zFxlpCtZgaX7XJbubICPnOKmqyZ8Hg",
    }
    get_response = requests.get(url, headers=headers)
    html = etree.HTML(get_response.text)
    pk = html.xpath('.//input[@id="pk"]/@value')
    pk = pk[0]
    token = html.xpath('.//input[@name="csrfmiddlewaretoken"]/@value')
    token = token[0]
    print("公钥:", pk)
    miwen_password = encrypto(pk, password)
    formdata = {
        'username': username,
        'password': miwen_password,
        'csrfmiddlewaretoken': token,
    }
    post_response = requests.post(url, headers=headers, data=formdata)
    print(post_response, post_response.text)

    cookies_dict = post_response.history[0].cookies.get_dict()
    cookies_str = json.dumps(cookies_dict)
    with open("cookies.txt", 'a', encoding='utf8') as file:
        file.write(cookies_str)
        file.write('\n')

    if post_response.status_code >= 400:
        with open('error.html', 'wb') as file:
            file.write(post_response.content)

if __name__ == "__main__":
    for user in users:
        username = user['username']
        password = user['password']
        main(username,password)