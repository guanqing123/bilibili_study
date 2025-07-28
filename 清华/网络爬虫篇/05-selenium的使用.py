import time
import requests
from selenium.webdriver.common.by import By


def requests_load_data():
    url = 'https://liuyan.people.com.cn/v1/threads/list/df'
    params = {
        "appCode": "PC42ce3bfa4980a9",
        "token": "",
        "signature": "9f41eaf88787382c14da461be7079546",
        "param": {
            "fid": "559",
            "showUnAnswer": 1,
            "typeId": 5,
            "lastItem": "",
            "position": 0,
            "rows": 10,
            "orderType": 2
        }
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Cookie': '__jsluid_s=0bcf223791c0bf5f9b6bd1fdd287d858; Hm_lvt_40ee6cb2aa47857d8ece9594220140f1=1753707498; HMACCOUNT=77C87CB738F2628D; language=zh-CN; deviceId=e5a54319-bead-44de-867a-65687cd37023; Hm_lpvt_40ee6cb2aa47857d8ece9594220140f1=1753707555',
        'Referer': 'https://liuyan.people.com.cn/threads/list?fid=559'
    }
    rep = requests.post(url, json=params, headers=headers)
    print(rep.json())


'''
1、selenium打开浏览器
2、访问要爬取的页面(操作页面)
3、获取页面的数据
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def selenium_load_data():
    # 1、selenium打开浏览器
    # s = Service('D\chromedriver.exe')
    # browser = webdriver.Chrome(service=s)
    s = Service('/usr/local/bin/chromedriver')
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=s, options=options)

    # 2、打开要操作的页面
    url = 'https://liuyan.people.com.cn/threads/list?fid=559'
    driver.get(url)
    time.sleep(5)

    print('地址:', driver.current_url)
    print('标题:', driver.title)

    # 3、获取页面数据
    html = driver.page_source
    # driver.refresh()
    # 保存页面源码
    with open('liuyan.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # 对当前页面截图
    driver.save_screenshot('liuyan.png')
    driver.quit()


def selenium_find_element():
    s = Service('/usr/local/bin/chromedriver')
    options = Options()
    options.add_argument("--start-maximized")
    # 创建一个driver对象(启动浏览器)
    driver = webdriver.Chrome(service=s, options=options)

    # 打开一个网页
    driver.get('https://www.baidu.com')

    # 通过xpath定位页面中id值为kw的元素
    ele = driver.find_element(By.XPATH, '//*[@id="kw"]')
    ele.send_keys("人大代表")

    # 关闭浏览器
    time.sleep(5)
    driver.quit()


def selenium_auto_login():
    s = Service('/usr/local/bin/chromedriver')
    options = Options()
    options.add_argument("--start-maximized")
    # 创建一个driver对象(启动浏览器)
    driver = webdriver.Chrome(service=s, options=options)

    driver.get('http://dev.sge.cn/hykj/index.html')
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@placeholder="请输入账号"]').send_keys('06407')
    driver.find_element(By.XPATH, '//*[@placeholder="请输入密码"]').send_keys('Gq@131625')

    driver.find_element(By.XPATH, '//button[@type="button"]').click()

    time.sleep(20)
    driver.quit()


if __name__ == '__main__':
    # requests_load_data()
    # selenium_load_data()
    # selenium_find_element()
    selenium_auto_login()