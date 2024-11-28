"""
continue的作用是用于跳过本次循环的后续代码,而继续执行下一次循环操
作,continue在循环中通常也是与if一起搭配使用

语法结构
for 循环变量 in 遍历对象:
    执行代码
    if 表达式:
        continue
"""
s = 0
for i in range(1, 101):
    if i % 2 == 1:
        continue
    else:
        s += i
else:
    print('1-100之间的偶数和', s)
