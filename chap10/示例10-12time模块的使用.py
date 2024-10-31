import time

now = time.time()
print(now)

# time.struct_time(tm_year=2024, tm_mon=10, tm_mday=28, tm_hour=12, tm_min=39, tm_sec=26, tm_wday=0, tm_yday=302, tm_isdst=0)
obj = time.localtime()  # struct_time对象
print(obj)

obj2 = time.localtime(60)  # 60秒 1970年,1月1日, 8时,1分,0秒
print(obj2)
print(type(obj2))
print('年份：', obj2.tm_year)
print('月份：', obj2.tm_mon)
print('日期：', obj2.tm_mday)
print('时：', obj2.tm_hour)
print('分：', obj2.tm_min)
print('秒：', obj2.tm_sec)
print('星期：', obj2.tm_wday)  # [0,6] 3表示是星期四 2表示星期三
print('今年的第几天：', obj2.tm_yday)
print(time.ctime())  # 时间戳对应的易读的字符串 Mon Oct 28 12:56:01 2024

# 日期时间格式化
print(time.strftime('%Y-%m-%d', time.localtime()))  # str---字符串,f--->format --time时间
print(time.strftime('%H:%M:%S', time.localtime()))
print('%B月份的名称：', time.strftime('%B', time.localtime()))
print('%A星期的名称：', time.strftime('%A', time.localtime()))

# 字符串转成struct_time
print(time.strptime('2024-10-28 13:03:10', '%Y-%m-%d %H:%M:%S'))

time.sleep(20)  # 休眠20秒
print('helloworld')
