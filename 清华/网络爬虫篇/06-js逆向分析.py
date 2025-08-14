import hashlib
import time

import requests


# 密码加密函数
def hasPwd(password):
    data_string = password + "Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z"
    obj = hashlib.md5()
    obj.update(data_string.encode('utf-8'))
    md5_string = obj.hexdigest()
    return md5_string


# 参数加密登录
def js_md5_login():
    url = "https://www.94mxd.com.cn/signin"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Referer": "https://www.94mxd.com.cn/signin",
        "Cookie": "SERVERID=e4ef0ed207aa77fa33d12fea4f834597|1753854491|1753853886"
    }

    json = {
        "email": "guanqinghz@163.com",
        "password": hasPwd("1234qwer")
    }
    resp = requests.post(url, json=json, headers=headers)
    print(f'resp.text = {resp.text}')
    print(f'resp.cookies = {resp.cookies.get_dict()}')


import execjs


# python调用js
def python_exec_js():
    js_code = """
        function add(a, b){
            return a + b
        }
        
        function work(){
            return 'python work'
        }
    """
    # 第一步：编译js代码
    JS = execjs.compile(js_code)
    # 调用
    res = JS.call('add', 10, 20)
    print(res)
    res = JS.call('work')
    print(res)


# 伪代码
def python_exec_js_file():
    name = input('请输入要翻译的内容:')
    with open('baidu.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    # 第1步：编译js代码
    JS = execjs.compile(js_code)
    # 调用
    sign = JS.call('b', name)

    params = {
        'from': 'zh',
        'to': 'en',
        'query': name,
        'simple_means_flag': '3',
        'sign': sign,
        'token': 'e4ef0ed207aa77fa33d12fea4f834597',
        'appid': '20230428001796405'
    }
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    resp = requests.get(url, params=params)
    print(f'resp.json = {resp.json()}')


def python_exec_js_file_2():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "Cookie": "__jsluid_s=0bcf223791c0bf5f9b6bd1fdd287d858; Hm_lvt_40ee6cb2aa47857d8ece9594220140f1=1753707498,"
                  "1753751547,1753796867,1755086940; Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1=1755086940; "
                  "HMACCOUNT=77C87CB738F2628D; language=zh-CN; deviceId=cfdc4c4b-001d-4bf7-89de-8989e39e687c",
        "Referer": "https://liuyan.people.com.cn/threads/list?fid=5050"
    }
    url = 'https://liuyan.people.com.cn/v1/threads/list/bw'
    json = {
        "appCode": "PC42ce3bfa4980a9",
        "param": "{\"fid\":5050,\"showUnAnswer\":1,\"typeId\":5,\"lastItem\":\"\",\"position\":1,\"rows\":10,"
                 "\"orderType\":2}",
        "signature": "22e8ff231248d4e2774c9d1b523afdf9",
        "token": ""
    }
    resp = requests.post(url, json=json, headers=headers)
    print(resp.text)


def md5_handle(pwd):
    """加密逆向还原"""
    str_pwd = pwd
    m5 = hashlib.md5()
    m5.update(str_pwd.encode('utf-8'))
    return m5.hexdigest()


def get_signature(lastItem):
    with open('liuyan.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    JS = execjs.compile(js_code)
    e = "/v1/threads/list/bw"
    t = {
        "fid": "5052",
        "showUnAnswer": 1,
        "typeId": 5,
        "lastItem": lastItem,
        "position": 1,
        "rows": 10,
        "orderType": 2
    }
    a = "PC42ce3bfa4980a9"
    l = md5_handle(a)[0:16]
    res = JS.call('i', e, t, l, '')
    signature = md5_handle(res)
    return t, signature


import json


def python_exec_js_file_3():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "Cookie": "__jsluid_s=0bcf223791c0bf5f9b6bd1fdd287d858; Hm_lvt_40ee6cb2aa47857d8ece9594220140f1=1753707498,"
                  "1753751547,1753796867,1755086940; Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1=1755086940; "
                  "HMACCOUNT=77C87CB738F2628D; language=zh-CN; deviceId=cfdc4c4b-001d-4bf7-89de-8989e39e687c",
        "Referer": "https://liuyan.people.com.cn/threads/list?fid=5050"
    }
    url = 'https://liuyan.people.com.cn/v1/threads/list/bw'
    param, signature = get_signature('')
    js = {
        "appCode": "PC42ce3bfa4980a9",
        "param": json.dumps(param, separators=(',', ':')),  # 将字典转换为JSON字符串
        "signature": signature,
        "token": ""
    }
    resp = requests.post(url, json=js, headers=headers)
    while True:
        if resultData := get_lastItem(resp):
            param, signature = get_signature(resultData)
            js = {
                "appCode": "PC42ce3bfa4980a9",
                "param": json.dumps(param, separators=(',', ':')),
                "signature": signature,
                "token": ""
            }
            resp = requests.post(url, json=js, headers=headers)
            # resp 响应吗不是200 退出循环
            if resp.status_code != 200:
                break
            print(f"resp= {resp.json()}")


def get_lastItem(resp):
    resultData = resp.json()['resultData']
    return resultData['lastItem']


def python_exec_js_file_4():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/111.0.0.0 Safari/537.36",
        "Cookie": "__jsluid_s=0bcf223791c0bf5f9b6bd1fdd287d858; Hm_lvt_40ee6cb2aa47857d8ece9594220140f1=1753707498,"
                  "1753751547,1753796867,1755086940; Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1=1755086940; "
                  "HMACCOUNT=77C87CB738F2628D; language=zh-CN; deviceId=cfdc4c4b-001d-4bf7-89de-8989e39e687c",
        "Referer": "https://liuyan.people.com.cn/threads/list?fid=5050"
    }
    url = 'https://liuyan.people.com.cn/v1/threads/list/bw'

    # 初始化lastItem为空字符串
    last_item = ""
    page_count = 0
    max_pages = 10  # 设置最大爬取页数，防止无限循环

    while page_count < max_pages:
        try:
            # 获取签名和参数
            param, signature = get_signature(last_item)

            # 构造请求数据，将param字典转换为JSON字符串
            js = {
                "appCode": "PC42ce3bfa4980a9",
                "param": json.dumps(param, separators=(',', ':')),
                "signature": signature,
                "token": ""
            }

            # 发送请求
            resp = requests.post(url, json=js, headers=headers, timeout=10)

            # 检查响应状态
            if resp.status_code != 200:
                print(f"请求失败，状态码: {resp.status_code}")
                break

            # 解析响应
            try:
                response_data = resp.json()
                print(f"第{page_count + 1}页数据: {response_data}")

                # 检查是否有数据
                if 'resultData' not in response_data or not response_data['resultData']:
                    print("没有更多数据了")
                    break

                # 获取下一页的lastItem
                result_data = response_data['resultData']
                if 'lastItem' not in result_data or not result_data['lastItem']:
                    print("没有更多分页数据了")
                    break

                last_item = result_data['lastItem']
                page_count += 1

                # 添加延时，避免请求过于频繁
                time.sleep(1)

            except json.JSONDecodeError:
                print("响应不是有效的JSON格式")
                print(f"响应内容: {resp.text}")
                break

        except requests.RequestException as e:
            print(f"请求发生错误: {e}")
            break
        except Exception as e:
            print(f"发生未知错误: {e}")
            break

    print(f"总共爬取了 {page_count} 页数据")


if __name__ == '__main__':
    # js_md5_login()
    # python_exec_js()
    # python_exec_js_file_2()
    # python_exec_js_file_3()
    python_exec_js_file_4()
