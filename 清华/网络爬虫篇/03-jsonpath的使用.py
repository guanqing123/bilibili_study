import json


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
