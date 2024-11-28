"""
continue的作用是用于跳过本次循环的后续代码,而继续执行下一次循环操
作,continue在循环中通常也是与if一起搭配使用

语法结构
while 表达式1:
    执行代码
    if 表达式2:
        continue
"""
i = 0
s = 0
while i <= 100:
    if i % 2 == 1:
        i += 1
        continue
    else:
        s += i
        i += 1
else:
    print("1-100之间的偶数和", s)
