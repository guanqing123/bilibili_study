import re

text = '小红小黄小李小花小强小赵小王小强小帅小美'
# 找数据的时候, 贪婪模式(没有?), 非贪婪模式
name = re.findall('小李(.*)小强', text)  # ['小花小强小赵小王']
print(name)
name = re.findall('小李(.*?)小强', text)  # ['小花']
print(name)

text = '小红/小黄/小李/小花/小倩/小雨'
name = re.findall('小黄/.*?/(.*?)/小倩', text)
print(name)
# 1、re.findall('前面(.*)后面', 目标字符串)
# 2、?非贪婪模式, 没有?贪婪模式
# 3、不确定的 匹配的时候不要括号!