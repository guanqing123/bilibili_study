from datetime import datetime  # 从datetime模块中 导入datetime类

dt = datetime.now()
print('当前的系统时间为：', dt) # 2025-07-02 08:42:27.247217
print('-'*40)

# datetime是一个类,手动创建这个类的对象
dt2 = datetime(2028, 8, 8, 20, 8)
#<class 'datetime.datetime'> dt2所表示的日期时间： 2028-08-08 20:08:00
print('dt2的数据类型', type(dt2), 'dt2所表示的日期时间：', dt2)
print('年：', dt2.year, '月：', dt2.month, '日：', dt2.day) #年： 2028 月： 8 日： 8
print('时：', dt2.hour, '分：', dt2.minute, '秒：', dt2.second)#时： 20 分： 8 秒： 0

dt = datetime(2025)
print(dt)

print('-'*40)
# 比较两个datetime类型对象的大小
labor_day = datetime(2028, 5, 1, 0, 0, 0)
national_day = datetime(2028, 10, 1, 0, 0, 0)
print('2028年5月1日比2028年10月1日早吗?', labor_day < national_day)  # True

print('-'*40)
# datetime类型与字符串进行转换
nowdt = datetime.now()
nowdt_str = nowdt.strftime('%Y/%m/%d %H:%M:%S')
# nowdt的数据类型： <class 'datetime.datetime'> nowdt所表示的数据是什么? 2025-07-02 10:19:53.262863
print('nowdt的数据类型：', type(nowdt), 'nowdt所表示的数据是什么?', nowdt)
# nowdt_str: <class 'str'> nowdt_str所表示的数据是什么? 2025/07/02 10:19:53
print('nowdt_str:', type(nowdt_str), 'nowdt_str所表示的数据是什么?', nowdt_str)

print('-'*40)
# 字符串类型转成datetime类型
str_datetime='2028年8月8日 20点8分'
dt3 = datetime.strptime(str_datetime, '%Y年%m月%d日 %H点%M分')
# dt3类型: <class 'datetime.datetime'> dt3: 2028-08-08 20:08:00
print('dt3类型:', type(dt3), 'dt3:', dt3)
