# 导入数据请求模块 (需要安装)
import requests
# 导入制表模块 (需要安装)
from prettytable import PrettyTable
# 导入json模块
import json
"""用户输入: 出发地+目的地+出发时间"""
from_city = input('请输入你要出发城市: ')
to_city = input('请输入目的城市: ')
# date = input('请输入时间: ')
date = '2024-06-25'
# 读取城市文件
f = open('city.json', encoding='utf-8').read()
# 把json字符串转成json字典
city_data = json.loads(f)
"""发送请求"""
# 模拟浏览器
headers = {
    'Cookie': '_uab_collina=170454776281977523056051; JSESSIONID=0ABD55424E0C9288A25FC32045334CB5; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toStation=%u5E7F%u5DDE%2CGZQ; route=9036359bb8a8a461c164a04f8f50b252; BIGipServerotn=3990290698.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromDate=2024-06-24; _jc_save_toDate=2024-06-19',
    # User-Agent 用户代理, 表示浏览器基本身份信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
# 请求网址
url = f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={city_data[from_city]}&leftTicketDTO.to_station={city_data[to_city]}&purpose_codes=ADULT'
# 发送请求
response = requests.get(url=url, headers=headers)
"""获取数据"""
# 获取响应的json数据
json_data = response.json()
"""解析数据"""
# 提取车次信息所在result列表
result = json_data['data']['result']
# 实例化对象
tb = PrettyTable()
# 设置字段名
tb.field_names = [
    '序号',
    '车次',
    '出发时间',
    '到达时间',
    '耗时',
    '特等座',
    '一等',
    '二等',
    '软卧',
    '硬卧',
    '硬座',
    '无座',
]
# 定义变量名
page = 1
# for循环遍历, 提取列表里面元素
for i in result:
    # 字符串分割 -> 返回列表
    index = i.split('|')
    num = index[3]  # 车次
    start_time = index[8]  # 出发时间
    end_time = index[9]  # 到达时间
    use_time = index[10]  # 耗时
    topGrade = index[32]  # 特等座
    first_class = index[31]  # 一等
    second_class = index[30]  # 二等
    hard_sleeper = index[28]  # 硬卧
    hard_seat = index[29]  # 硬座
    no_seat = index[26]  # 无座
    soft_sleeper = index[23]  # 软卧
    tb.add_row([
        page,
        num,
        start_time,
        end_time,
        use_time,
        topGrade,
        first_class,
        second_class,
        soft_sleeper,
        hard_sleeper,
        hard_seat,
        no_seat,
    ])
    page += 1

print(tb)
num = input('请输入你要购买车次序号: ')