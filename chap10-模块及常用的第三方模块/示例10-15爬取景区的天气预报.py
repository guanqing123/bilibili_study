import requests

url = 'https://www.weather.com.cn/weather1d/101010100.shtml'  # 爬虫打开的浏览器上的网页
resp = requests.get(url)  # 打开浏览器并打开网址
# 设置一下编码格式
resp.encoding = 'utf-8'
print(resp.text)  # resp响应对象,对象名.属性名 resp.text

import re

city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', resp.text)
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', resp.text)
wd = re.findall('<span class="wd">(.*)</span>', resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', resp.text)
print(type(city), city)  # <class 'list'> ['景区', '三亚', '九寨沟', '大理', '张家界', '桂林', '青岛']
print(weather)  # ['天气', '多云', '阴转多云', '小雨转阴', '多云', '多云转阵雨', '多云']
print(wd)  # ['气温', '33/27℃', '29/14℃', '21/17℃', '37/25℃', '37/27℃', '30/26℃']
print(zs)  # ['旅游指数', '较适宜', '适宜', '适宜', '较不宜', '较不宜', '适宜']

print('-' * 40)
lst = []
for a, b, c, d in zip(city, weather, wd, zs):
    lst.append([a, b, c, d])
print(lst)
for item in lst:
    print(item)

'''
<span class="name">三亚</span>
<span class="weather">雷阵雨</span>
<span class="wd">27/22℃</span>
<span class="zs">一般</span>
'''
