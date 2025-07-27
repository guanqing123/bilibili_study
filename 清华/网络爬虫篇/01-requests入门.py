import json
import time

import requests


def get_response():
    url = "https://www.baidu.com/"
    cookies = {"name": "cookie-test"}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers, cookies=cookies)
    # 方式一：resp.text 获取到的是字符串
    print(resp.text)

    # 方式二：resp.content 获取到的是原始的二进制数据(bytes)
    # decode() 二进制转字符串
    print(resp.content.decode())

    # 获取响应码
    print(resp.status_code)
    # 获取响应头
    print(f'响应头 : {resp.headers}')
    print(type(resp.cookies), resp.cookies)

    # 获取请求头
    # {'User-Agent': 'python-requests/2.32.3',
    #  'Accept-Encoding': 'gzip, deflate, br',
    #  'Accept': '*/*',
    #  'Connection': 'keep-alive',
    #  'Cookie': 'name=cookie-test'}
    print(resp.request.headers)
    # 获取请求cookies
    # print(resp.request._cookies)


def download_html():
    url = "https://www.baidu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    # 发送请求获取响应信息
    resp = requests.get(url=url, headers=headers)

    # 下载网页
    with open("baidu.html", "w", encoding="utf-8") as f:
        f.write(resp.content.decode())


def download_image():
    url = "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    # 下载图片
    with open("baidu.png", "wb") as f:
        f.write(resp.content)


def download_mp3():
    # 下载网易云音乐
    url = ("https://m804.music.126.net/20250725091320/0a068004683dee9d4711ff2b0c492da9/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj"
           "/18192765420/f612/0439/b743/04d72caccf53a1ef68eeeff0bd4e6fbd.m4a?vuutv"
           "=MBsnZwP9hjPZmFeTesYemuidGuOCwaTLFC7NbWens1bYErJkk/6+oLvtHRDgIaYIArZ4uzBtzmqTU7eRi4Ap"
           "+Hk3XXsOwivZvvsxaBsNLiU"
           "=&authSecret=000001983f0d686d16eb0a32b0150006")

    resp = requests.get(url=url)
    with open("wy.mp3", "wb") as f:
        f.write(resp.content)


# requests请求传递查询参数
# 方式一: 参数直接拼接在url后面
def requests_get():
    url = "https://www.baidu.com/s?wd=长城"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)
    print(resp.content.decode())


# 方式二: 通过params参数传递
# 请求地址:
def requests_get_params():
    url = "https://www.baidu.com/s"
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    # 请求参数
    params = {
        "wd": "长城"
    }
    resp = requests.get(url=url, headers=headers, params=params)
    print(resp.content.decode())


"""
发送post请求的方法：
    requests.post()
参数传递：
    1、表单参数: form-data
        requests.post(url,data=字典参数)
    2、json参数:
        requests.post(url,json=字典参数)     
"""


# 案例一：百度翻译发送post请求 传递表单参数
def post_data():
    url = "https://fanyi.baidu.com/sug"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    params = {
        "kw": "hello"
    }
    resp = requests.post(url=url, data=params, headers=headers)
    print(f'resp.json = {resp.json()}')
    print(f'resp.content = {resp.content.decode("unicode_escape")}')


def post_json():
    url = 'http://dev.sge.cn/rest/login'
    json = {
        "khdm": "34010230",
        "loginid": "admin",
        "password": "Hongyan@123"
    }
    resp = requests.post(url=url, json=json)
    print(f'resp.json = {resp.json()}')


'''
1、通过控制台抓包:
    登录的url地址：
    登录时传递的参数:
    请求方法:
    
2、网站用户鉴权的方式
    网站的后台服务校验用户是否登录的方法:
    1、cookie + session去登录
    2、通过token鉴权(一般常用于前后端分离的项目)
    
3、实现步骤:
    1、使用cookie+session鉴权的网站模拟登录的流程
        1、传递账号密码,进行登录
        2、登录之后保存cookie(返回时在响应头的set-cookie字段中)
        3、请求其他页面时，携带cookie
        
    2、使用token鉴权的网站模拟登录的流程
        1、传递账号密码,进行登录
        2、登录之后保存token(返回的时候,在响应体中)
        3、请求其他页面时，携带token
'''


def login_cookie():
    login_url = 'https://passport.china.com/logon'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36',
        'Referer': 'https://passport.china.com/logon',
        'Cookie': 'SESSION_COOKIE=128'
    }
    params = {
        'userName': '17775990925',
        'password': 'a546245426',
    }

    response = requests.post(url=login_url, data=params, headers=headers)
    print(response.cookies)

    # ==============方式一: 以字符串格式传递cookie===========================
    # 获取cookie信息
    url = 'https://passport.china.com'
    response = requests.get(url, headers=headers, cookies=response.cookies)
    print(f'登录成功:{response.content.decode()}')


'''
方式一：以字典方式传递
    cookies = {}
    requests.get(cookies=cookies)
方式二：以字符串格式传递 浏览器直接复制
    headers = {
        'Cookie':'字符串格式cookie值'
    }
方式三：requests.session

'''


def login_session():
    # 1、使用requests.session创建一个请求的对象
    http = requests.session()
    # 2、发送请求进行登录
    login_url = 'https://passport.china.com/logon'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/131.0.0.0 Safari/537.36',
        'Referer': 'https://passport.china.com/logon'
    }
    params = {
        'userName': '17775990925',
        'password': 'a546245426',
    }
    resp = http.post(url=login_url, headers=headers, data=params)
    print(resp.content.decode())
    # 请求需要登录的页面
    resp = http.get('https://passport.china.com', headers=headers)
    print(resp.content.decode())


def load_ajax(pageIndex):
    file = open('岗位.txt', 'a', encoding='utf-8')
    timestamp = int(time.time() * 1000)
    url = (f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}&countryId=2,11,6,5,'
           f'10&cityId=7,2,3,5,1,8,37,46&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword='
           f'&pageIndex={pageIndex}&pageSize=10&language=zh-cn&area=cn')
    resp = requests.get(url)

    # 获取返回的json数据：使用json方法获取响应的json数据会自动转换为字典
    result = resp.json()
    # 获取所有的岗位数据
    Posts = result['Data']['Posts']

    print(f'正在爬取第{pageIndex}页数据')
    for post in Posts:
        print(post['RecruitPostName'], post['ProductName'], post['CategoryName'], post['Responsibility'])
        # file.write(str(post) + '\n')
        file.writelines([str(post)])
    print(f'-------------------------------------{pageIndex}结束---------------------------------------')
    file.close()


#  将文件中json数据读取转换为python对象方式一
def json_loads():
    with open('datas.json', 'r', encoding='utf-8') as file:
        str_data = file.read()
        print(type(str_data), str_data)  # <class 'str'>
        json_data = json.loads(str_data)
        print(type(json_data), json_data)  # <class 'dict'>


# {'name': '张三', 'age': 18, 'skill': ['java', 'python', 'c++'], 'isDelete': True, 'isActive': False, 'addr': {'city':
# '上海', 'street': '上海路'}, 'phone': None}

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
    json.dump(data, open('dump.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # for i in range(1, 10):
    #     load_ajax(i)

    json_loads()
    # json_load()
    # json_dumps()
    # json_dump()
