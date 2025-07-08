import time

now = time.time()
print(now)  # 1751375379.086664

# time.struct_time(tm_year=2025, tm_mon=7, tm_mday=1, tm_hour=21, tm_min=9, tm_sec=50, tm_wday=1, tm_yday=182, tm_isdst=0)
obj = time.localtime()  # struct_time对象
print(obj)

obj2 = time.localtime(now)  # 60秒 1970年,1月1日, 8时,1分,0秒
print(obj2)  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=1, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(type(obj2))  # <class 'time.struct_time'>
print('年份：', obj2.tm_year)  # 1970
print('月份：', obj2.tm_mon)  # 1
print('日期：', obj2.tm_mday)  # 1
print('时：', obj2.tm_hour)  # 8
print('分：', obj2.tm_min)  # 1
print('秒：', obj2.tm_sec)  # 0
print('星期：', obj2.tm_wday)  # 3 [0,6] 3表示是星期四 2表示星期三
print('今年的第几天：', obj2.tm_yday)  # 1
print(time.ctime())  # 时间戳对应的易读的字符串 Tue Jul  1 21:11:49 2025

# 日期时间格式化
print(time.strftime('%Y-%m-%d', time.localtime()))  # str---字符串,f--->format --time时间 2025-07-01
print(time.strftime('%H:%M:%S', time.localtime()))  # 21:12:22
print('%B月份的名称：', time.strftime('%B', time.localtime()))  # July
print('%A星期的名称：', time.strftime('%A', time.localtime()))  # Tuesday

# 字符串转成struct_time
# time.struct_time(tm_year=2024, tm_mon=10, tm_mday=28, tm_hour=13, tm_min=3, tm_sec=10, tm_wday=0, tm_yday=302, tm_isdst=-1)
print(time.strptime('2024-10-28 13:03:10', '%Y-%m-%d %H:%M:%S'))

time.sleep(20)  # 休眠20秒
print('helloworld')
