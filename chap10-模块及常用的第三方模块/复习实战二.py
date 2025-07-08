from datetime import datetime, timedelta

date = input('请输入开始日期：')
delta = input('请输入间隔天数：')

start = datetime.strptime(date, '%Y-%m-%d')
end = start + timedelta(days=int(delta))
print('开始日期：', start)
print('结束日期：', end)