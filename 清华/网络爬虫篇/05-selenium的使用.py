import random
import time

import pandas as pd
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# requests 加载数据
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


# selenium 加载数据
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


# selenium 查找元素
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


# selenium 自动登录
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


def selenium_fetch_data():
    s = Service('/usr/local/bin/chromedriver')
    options = Options()
    options.add_argument("--start-maximized")
    # 创建一个driver对象(启动浏览器)
    driver = webdriver.Chrome(service=s, options=options)

    driver.get('https://liuyan.people.com.cn/threads/list?fid=559')
    time.sleep(5)

    # 1、先定位到包含所有元素的数据的li列表
    li_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')
    # 2、遍历页面上所有的li标签(元素)
    for item in li_list:
        title = item.find_element(By.XPATH, './div[@class="tabList fl"]/h1').text
        pub_time = item.find_element(By.XPATH, './/div[@class="headMainS fl"]/p').text
        content = item.find_element(By.XPATH, './p[@class="replyContent"]/span[1]').text
        print(f'标题:{title} \t 发布时间:{pub_time} \t 内容:{content}')


def selenium_ys_wait():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)
    time.sleep(3)
    driver.get('https://mail.qq.com/')
    # 隐式等待
    driver.implicitly_wait(10)
    # Message: no such element iframe标签的原因
    driver.find_element(By.XPATH, "//*[@id='switcher_plogin']").click()

    time.sleep(10)
    driver.quit()


# 显式等待
def selenium_xs_wait():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)
    # 第一步: 创建一个等待对象
    wait = WebDriverWait(driver, 30, 0.2)
    # 第二步: 定义元素查找对象
    # located = ("定位方式", '定位表达式')
    # 比如通过xpath
    located = (By.XPATH, '//input[@id="u"]')
    # 第三步: 定位的等待条件
    conditions = EC.visibility_of_element_located(located)
    # 第四步: 通过等待计时器对象去找
    wait.until(conditions)

    # # 一行代码表示
    # WebDriverWait(driver, 30, 0.2).until(
    #     EC.visibility_of_element_located(
    #         (By.XPATH, '//input[@id="u"]')
    #     )
    # )


#  切换iframe
def selenium_iframe():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)
    time.sleep(3)
    driver.get('https://mail.qq.com/')
    # 隐式等待
    # driver.implicitly_wait(10)

    # 切换到要操作的iframe
    driver.switch_to.frame(1)
    driver.switch_to.frame('ptlogin_iframe')

    # Message: no such element iframe标签的原因
    driver.find_element(By.XPATH, "//*[@id='switcher_plogin']").click()

    time.sleep(10)
    driver.quit()


# 显示等待, 切换两级iframe, 切回默认的HTML
def selenium_qq_mail_login():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)

    driver.get('https://mail.qq.com/')

    # 显示等待 30秒, 每0.2秒检查一次 看看iframe是否可见
    WebDriverWait(driver, 30, 0.2).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//iframe[@class='QQMailSdkTool_login_loginBox_qq_iframe']")
        )
    )

    # 第一个 iframe 切换 通过element元素去进行切换
    ele_iframe = driver.find_element(By.XPATH, "//iframe[@class='QQMailSdkTool_login_loginBox_qq_iframe']")
    driver.switch_to.frame(ele_iframe)

    # 第二个 iframe 切换 通过iframe的名字（name属性）进行切换
    driver.switch_to.frame("ptlogin_iframe")
    driver.find_element(By.XPATH, "//a[@id='switcher_plogin']").click()

    driver.find_element(By.XPATH, "//input[@id='u']").send_keys("374052753@qq.com")
    driver.find_element(By.XPATH, "//input[@id='p']").send_keys("123456")

    driver.find_element(By.XPATH, "//input[@id='login_button']").click()

    # 切换回默认的HTML页面中
    driver.switch_to.default_content()
    time.sleep(5)
    driver.quit()


def selenium_scroll():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)

    # 打开目标网站
    driver.get('https://liuyan.people.com.cn/threads/list?fid=1007')
    # 设置隐式等待时间
    driver.implicitly_wait(10)

    while True:
        try:
            # 随机停留个2-5秒
            time.sleep(random.randint(2, 5))
            # 定位查看更多的元素
            ele = driver.find_element(By.XPATH, "//div[@class='mordList']")
            res = ele.location_once_scrolled_into_view
            print('滚动之后的坐标:', res)
            ele.click()
        except:
            break

    # 用于存储所有数据的列表
    data_list = []

    # 1、先定位到包含所有元素的数据的li列表
    li_list = driver.find_elements(By.XPATH, '//ul[@class="replyList"]/li')
    # 2、遍历页面上所有的li标签(元素)
    for item in li_list:
        title = item.find_element(By.XPATH, './div[@class="tabList fl"]/h1').text
        pub_time = item.find_element(By.XPATH, './/div[@class="headMainS fl"]/p').text
        content = item.find_element(By.XPATH, './p[@class="replyContent"]/span[1]').text
        print(f'标题:{title} \t 发布时间:{pub_time} \t 内容:{content}')

        # 将数据添加到列表中
        data_list.append({
            '标题': title,
            '发布时间': pub_time,
            '内容': content
        })

    # 使用pandas创建DataFrame并保存到Excel文件
    df = pd.DataFrame(data_list)
    df.to_excel('liuyan_data.xlsx', index=False)

    # 10秒之后关闭页面
    time.sleep(10)
    driver.quit()


# js 每隔一段时间,滚动一段距离
def selenium_js_scroll():
    s = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=s)

    # 打开目标网站
    driver.get('https://liuyan.people.com.cn/threads/list?fid=1007')
    # 设置隐式等待时间
    driver.implicitly_wait(10)

    total = 0
    for i in range(5):
        # 休眠0-1秒
        time.sleep(random.random())
        total += random.randint(100, 300)
        js = 'window.scrollTo(0, {})'.format(total)
        # 通过driver执行js代码
        driver.execute_script(js)

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    # requests_load_data()
    # selenium_load_data()
    # selenium_find_element()
    # selenium_auto_login()
    # selenium_fetch_data()
    # selenium_ys_wait()
    # selenium_iframe()
    # selenium_qq_mail_login()
    # selenium_scroll()
    selenium_js_scroll()