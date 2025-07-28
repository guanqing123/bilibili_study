import json
import time

import requests


#  将文件中json数据读取转换为python对象方式一
def json_loads():
    with open('datas.json', 'r', encoding='utf-8') as file:
        str_data = file.read()
        print(type(str_data), str_data)  # <class 'str'>
        # 将json数据转换为python对象
        json_data = json.loads(str_data)
        print(type(json_data), json_data)  # <class 'dict'>


# 将文件中json数据读取转换为python对象方式二
def json_load():
    # 将 json 文件转成 python 对象
    json_str = json.load(open('datas.json', 'r', encoding='utf-8'))
    print(type(json_str), json_str)  # <class 'dict'>


# 将python的数据写入json文件的方式一
def json_dumps():
    data = {
        'name': '张三',
        'age': 18,
        'skill': ['java', 'python', 'c++'],
        'isDelete': True,
        'isActive': False,
        'addr': {
            'city': '上海',
            'street': '上海路'
        },
        'phone': None
    }
    print(type(data))
    # 将python的数据转换为json字符串
    json_str = json.dumps(data, ensure_ascii=False, indent=4)
    print(type(json_str), json_str)
    with open('write.json', 'w', encoding='utf-8') as file:
        file.write(json_str)


# 将python的数据写入json文件的方式二
def json_dump():
    data = {
        'name': '张三',
        'age': 18,
        'skill': ['java', 'python', 'c++'],
        'isDelete': True,
        'isActive': False,
        'addr': {
            'city': '上海',
            'street': '上海路'
        },
        'phone': None
    }
    # 将python对象写入文件
    json.dump(data, open('dump.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


'''
    安装jsonpath: pip3 install jsonpath
'''

from jsonpath import jsonpath


def use_jsonpath():
    json_data = json.load(open('data.json', 'r', encoding='utf-8'))
    # 使用jsonpath提取数据
    title = jsonpath(json_data, '$.title')
    name = jsonpath(json_data, '$..name')
    photo = jsonpath(json_data, '$.author.photo')
    time = jsonpath(json_data, '$.time')

    print(title, name, photo, time)


# 小饭桌
def jsonpath_xfz(page):
    url = "https://www.xfz.cn/api/website/articles/?p={}&n=20&type=%E7%83%AD%E7%82%B9".format(page)

    resp = requests.get(url)
    result = resp.json()

    # 遍历所有的咨询信息,提取数据
    for item in result['data']:
        title = jsonpath(item, '$.title')[0]
        name = jsonpath(item, '$..name')[0]
        photo = jsonpath(item, '$.author.photo')[0]
        stime = jsonpath(item, '$.time')[0]
        print(title, name, photo, stime)
    time.sleep(1)


if __name__ == '__main__':
    for i in range(1, 5):
        jsonpath_xfz(i)
