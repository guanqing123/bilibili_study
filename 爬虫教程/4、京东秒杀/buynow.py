import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# windows
# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# macos pip3 show pyttsx3
import pyttsx3


# 文本转语言设置
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 调整语速
    engine.setProperty('volumn', 0.9)  # 调整音量
    engine.say(text)
    engine.runAndWait()


# 打开浏览器
# s = Service('D\chromedriver.exe')
# browser = webdriver.Chrome(service=s)
s = Service('/usr/local/bin/chromedriver')
options = Options()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(service=s, options=options)

# 进入京东网页
browser.get("https://www.jd.com/")
time.sleep(60)
print('-'*40)

# 扫码登录
# browser.find_element(By.LINK_TEXT, "你好，请登录").click()
# print(f'请扫码')
# time.sleep(15)
# 获取 Cookies 并添加到当前会话
cookies = browser.get_cookies()  # 获取当前浏览器的 cookies
for cookie in cookies:
    browser.add_cookie(cookie)  # 添加每个 cookie 到浏览器

# 刷新页面，确保登录状态已生效
browser.refresh()
time.sleep(5)

# 打开购物车页面
browser.get('https://cart.jd.com/cart_index')
time.sleep(10)

# 获取页面内容（如果页面加载了内容）
page_content = browser.page_source
print(page_content)

# 全选购物车
# while True:
#     if browser.find_element(By.CLASS_NAME, 'jdcheckbox'):
#         browser.find_element(By.CLASS_NAME, 'jdcheckbox').click()
#         break
#
# while True:
#     # 获取电脑现在的时间
#     now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#     # 对比时间,时间到的话点击结算
#     print(now)
#     # 判断是不是到了秒杀时间？
#     if now >= '2024-11-13 20:59:00':
#         # 点击结算按钮
#         while 1 == 1:
#             try:
#                 if browser.find_element(By.LINK_TEXT, '去结算'):
#                     print('here')
#                     browser.find_element(By.LINK_TEXT, '去结算').click()
#                     print(f'主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单')
#                     speak(f'主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单')
#                     break
#                     # windows
#                     # speaker.Speak(f'主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单')
#             except:
#                 pass
#         # 点击提交订单按钮
#         while True:
#             try:
#                 if browser.find_element(By.LINK_TEXT, '提交订单'):
#                     browser.find_element(By.LINK_TEXT, '提交订单').click()
#                     print(f'主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单')
#                     speak(f'主人,结算提交成功,我已帮你抢到商品啦,请及时支付订单')
#                     break
#             except:
#                 pass
