import requests
import json
#vercel这个用vercel url 但是说实话，成功率感人
def dataget():
    # 目标URL
    url = "https://tuu-yangfreeyyds-projects.vercel.app"

    # 请求头，指定Content-Type为application/json
    headers = {
        "Content-Type": "application/json"
    }

    # 请求体数据
    data = {
        "url": "https://www.douyin.com/aweme/v1/web/aweme/detail/?aid=6383&version_name=19.6.0&device_platform=webapp",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))
    # 提取
    data = response.json()
    data = data.get("data")
    xbogus = data.get('xbogus')
    mstoken = data.get('mstoken')
    ttwid = data.get('ttwid')
    return xbogus,mstoken,ttwid

print(dataget())