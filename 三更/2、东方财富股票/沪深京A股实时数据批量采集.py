import re
import requests
import pandas

'''
东方财富网沪深京A股数据的网址。

1.东方财富网首页 -- 东方财富特色服务 -- 沪深京 -- 行情中心 -- 沪深京个股 -- 沪深京A股。
2.打开开发者工具 -- 网路 -- 全部 -- 刷新。
3.放大镜里面搜索股票关键字 -- 点进去 -- 在标头中复制链接。
'''

stocks = []  # 空数据

wz = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/130.0.0.0 Safari/537.36'}

for pn in range(1, 284):
    url = (f'https://45.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112409084948914357653_1730350196663&pn={pn}&pz'
           f'=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&dect=1&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t'
           f':6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,'
           f'f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1730350196664')
    res = requests.get(url, headers=wz)

    # 筛选数据
    name = re.findall('"f14":"(.*?)",', res.text)  # 名称
    code = re.findall('"f12":"(.*?)",', res.text)  # 代码
    last_new_price = re.findall('"f2":(.*?),', res.text)  # 最新价

    # 组合数据
    for i in range(len(name)):
        stock = [name[i], code[i], last_new_price[i]]
        stocks.append(stock)

# 转化成表格数据
data = pandas.DataFrame(stocks)
data.to_excel('A股实时数据.xlsx', index=False, header=['名称', '代码', '最新价'])
