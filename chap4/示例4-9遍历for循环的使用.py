# 遍历字符串
for i in 'hello':
    print(i)
# range()函数,Python中的内置函数,产生一个[n,m)的整数序列,包含n,但不包含m
for i in range(1, 11):
    # print(i)
    if i % 2 == 0:
        print(i, '是偶数')
# 计算1-10之间的累计和
s = 0
for i in range(1, 11):
    s += i
print('1-10之间的累加和为:', s)
print('-' * 10 + '100到999之间的水仙花数' + '-' * 10)
'''
153=3*3*3+5*5*5+1*1*1
'''
for i in range(100, 1000):
    s = str(i)
    a = eval(s[0])
    b = eval(s[1])
    c = eval(s[2])
    if a * a * a + b * b * b + c * c * c == i:
        print(i, '是水仙花数')

for i in range(100, 1000):
    s = str(i)
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if a * a * a + b * b * b + c * c * c == i:
        print(i, '是水仙花数')

for i in range(100, 1000):
    sd = i % 10  # 获取个位上的数字  假设 153%10 -->3
    tens = i // 10 % 10  # 获取十位上的数字 153//10 --> 15 15%10-->5
    hundred = i // 100  # 获取百位上的数字 153//100-->1
    if sd * sd * sd + tens * tens * tens + hundred * hundred * hundred == i:
        print(i, '是水仙花数')
