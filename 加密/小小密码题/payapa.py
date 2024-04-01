import requests
import pymysql
from lxml import etree

my_result = {}
url_list=["16","15","/14","/13","/12","/11","/10","/9","/8","/7","/6","/5","/4","/3","/2","/1"]
connection = pymysql.connect(
    host='154.8.165.65',
    user='henu',
    password='fp2Er4j3S4rW5mdi',  #实验室的密码，不好公布大家
    database='henu',
    port=3306
)
cursor = connection.cursor()


def joint_String(my_list):
    merged_list = []
    for i in range(0, len(my_list), 2):
        if i + 1 < len(my_list):
            merged_list.append(my_list[i] +'?'+ my_list[i + 1])
    return merged_list


def students_massage():
    resp = requests.get(url + plus1)
    resp.encoding = "Utf-8"
    return resp.text


def teachers_massage():
    resp = requests.get(url + plus2)
    resp.encoding = "Utf-8"
    return resp.text

for i in url_list:
    url="https://jwc.henu.edu.cn/"
    plus1="jwzl/xszl"+i+".htm"
    plus2="jwzl/jszl"+i+".htm"

    et = etree.HTML(students_massage())
    ost_list = et.xpath("//div[@id='middle']//span//text()")
    ost_url_list = et.xpath("//div[@id='middle']//a/@href")
    nst_list=ost_list[6:-2]
    nst_list=joint_String(nst_list)
    nst_url_list=ost_url_list[5:-2]

    nnst_url_list = []

    for item in nst_url_list:
        nnst_url_list.append("https://jwc.henu.edu.cn/"+item.replace("..",""))

        my_dict = {key: value for key, value in zip(nst_list,nnst_url_list)}
        my_result.update(my_dict)

cursor = connection.cursor()

for key, value in my_result.items():
    parts = key.split('?')
    name = parts[0]
    time = parts[1]
    sql = "INSERT INTO ma (name, time,url) VALUES (%s, %s, %s)"
    values = (name,time,value)
    cursor.execute(sql, values)
    print("已提交一行数据")
connection.commit()
connection.close()