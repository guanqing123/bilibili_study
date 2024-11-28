import requests
from prettytable import PrettyTable

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/130.0.0.0 Safari/537.36',
           'cookie': '_uab_collina=173133642754393634271524; JSESSIONID=E1D5C346E2AD464D61B9F2D5073CB953; '
                     'BIGipServerotn=602407178.50210.0000; guidesStatus=off; highContrastMode=defaltMode; '
                     'cursorStatus=off; BIGipServerpassport=786956554.50215.0000; '
                     'route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u676D%u5DDE%2CHZH; '
                     '_jc_save_toStation=%u8862%u5DDE%2CQEH; _jc_save_toDate=2024-11-11; _jc_save_wfdc_flag=dc; '
                     '_jc_save_fromDate=2024-11-12'}

url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2024-11-12&leftTicketDTO.from_station=HZH'
       '&leftTicketDTO.to_station=QEH&purpose_codes=ADULT')

res = requests.get(url, headers=headers)

json_data = res.json()
# 实例化对象
tb = PrettyTable()
# 设置字段名
tb.field_names = ['序号', '车次', '出发时间', '到达时间', '耗时', '特等座', '一等', '二等', '硬卧', '硬座', '无座',
                  '软卧']
# 设置序号
page = 1
# 提取车次信息所在列表
result = json_data['data']['result']
for i in result:
    # 字符串分割
    index = i.split('|')
    num = index[3]  # 车次
    start_time = index[8]  # 出发时间
    end_time = index[9]  # 达到时间
    use_time = index[10]  # 耗时
    topGrade = index[32]  # 特等座
    first_class = index[31]  # 一等
    second_class = index[30]  # 二等
    hard_class = index[28]  # 硬卧
    hard_seat = index[29]  # 硬座
    no_seat = index[26]  # 无座
    soft_sleeper = index[23]  # 软卧
    # page = 0
    '''为了方便查看索引位置'''
    # for j in index:
    #     print(page, j, sep='****')
    #     page += 1
    # 添加字段内容
    tb.add_row(
        [page, num, start_time, end_time, use_time, topGrade, first_class, second_class, hard_class, hard_seat, no_seat,
         soft_sleeper])
    page += 1
print(tb)
