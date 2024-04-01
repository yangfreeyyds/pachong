import asyncio
import json
import random
import requests
import urllib.parse
from openpyxl import load_workbook
#逆向xbogus,ttwid
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
#暂时没用
def get_ms_token():
    """
    根据传入长度产生随机字符串
    """
    randomlength = 107
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789='
    length = len(base_str) - 1
    for _ in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

#print(get_ms_token())

def payapa(keyword):
    encoded_keyword = urllib.parse.quote(keyword, encoding='utf-8')
    offset = 0
    sum = 0
    count = 0
    xbogus, mstoken, ttwid = dataget()
    while offset < 49:
        if count == 20:
            xbogus, mstoken, ttwid = dataget()
            count = 0
        url = "https://www.douyin.com/aweme/v1/web/general/search/single/"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Cookie': 'xbogus='+xbogus+'; mstoken='+mstoken+'; ttwid='+ttwid+'; IsDouyinActive="true"; ',
            # 'Cookie': '__ac_nonce=0660fad8700bc0118153; __ac_signature=_02B4Z6wo00f01mvyBagAAIDDKMKcyhGJ8B5rwiEAAP0C94; SEARCH_RESULT_LIST_TYPE=%22single%22; ttwid=1%7C0niGoYF4S3w-c4NWj3rgCcc3762H08TSb8VU8u0mdXA%7C1712303495%7C94211a887138f2a34721350081eae806cdbdd263f85e1e306270d1c61003f3bc; home_can_add_dy_2_desktop=%220%22; IsDouyinActive=true; csrf_session_id=a652f0fad14330c0dccc7b46a3047ffe; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; msToken=AMKz8pJMzmiaCSB8bv891ewgHONhyp07GiLcGkcGR9NmR73rtClC10HHcP7y5hctciTa4I77cwcUlD37BwnK57wuvEADaOk3S2CSUCVC5sn0R3lMlehBmtPiHdsXWQq3; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D',
            'Host': 'www.douyin.com',
            'Referer': 'https://www.douyin.com/search/' + encoded_keyword + '?type=general',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }
        params = {
            "device_platform": "webapp",
            "aid": "6383",
            "channel": "channel_pc_web",
            "search_channel": "aweme_general",
            "enable_history": "1",
            "filter_selected": '{"sort_type":"1","publish_time":"0"}',
            "keyword": keyword,
            "search_source": "tab_search",
            "query_correct_type": "1",
            "is_filter_search": "1",
            "from_group_id": "",
            "offset": offset,
            "count": "10",
            "need_filter_settings": "1",
            "pc_client_type": "1",
            "version_code": "190600",
            "version_name": "19.6.0",
            "cookie_enabled": "true",
            "screen_width": "1920",
            "screen_height": "1080",
            "browser_language": "en-US",
            "browser_platform": "Win32",
            "browser_name": "Firefox",
            "browser_version": "118.0",
            "browser_online": "true",
            "engine_name": "Gecko",
            "engine_version": "109.0",
            "os_name": "Windows",
            "os_version": "10",
            "cpu_core_num": "16",
            "device_memory": "",
            "platform": "PC",
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        for item in data.get("data", []):
            try:
                aweme_info = item.get("aweme_info", {})
                # 注意：如果aweme_info不是字典，下一行将抛出异常
                statistics = aweme_info.get("statistics", {})
                # 确保 'digg_count' 存在并且是整数，否则使用默认值 0
                digg_count = int(statistics.get('digg_count', 0))
                sum += digg_count
            except ValueError:
                # 如果digg_count不是一个可以转换为整数的值，打印错误并跳过
                print("ValueError: digg_count could not be converted to an integer.")
            except TypeError:
                # 如果aweme_info或statistics不是预期的字典类型，打印错误并跳过
                print("TypeError: Expected a dictionary but got a different type.")
            except Exception as e:
                # 捕获其他所有异常，打印错误信息并跳过
                print(f"Unexpected error: {e}")
        if sum == 0:
            print(count)
            count += 1
            continue
        else:
            offset += 10
            count += 1
            # txt相比于excel要快很多所以就用txt保存了
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{sum} {keyword}\n")


#async def main():
    #wb = load_workbook(filename='皖宁鲁冀藏苏_乡镇汇总.xlsx')
    #ws = wb.active
    #keywords = [row[2] for row in ws.iter_rows(min_row=2, values_only=True) if row[0]]
    # 每5个关键字分成一组
    #group_size = 5
    #for i in range(0, len(keywords), group_size):
        #group = keywords[i:i+group_size]
        #tasks = [payapa(keyword) for keyword in group]
        #await asyncio.gather(*tasks)
        # await asyncio.sleep(1)
#asyncio.run(main())

wb = load_workbook(filename='皖宁鲁冀藏苏_乡镇汇总.xlsx')
ws = wb.active
keywords = [row[2] for row in ws.iter_rows(min_row=2, values_only=True) if row[0]]
for keyword in keywords:
    payapa(keyword)




