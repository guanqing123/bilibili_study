# 常用的字符串操作
# x+y 将字符串 x 与 y 连接起来
# x*n 或 n*x 复制 n 次字符串 x
# x in s 如果x是s的子串，结果为True，否则结果为False

x = '2022年'
y = '北京冬奥会'
print(x + y)  # 连接两个字符
print(x * 10)  # 对x这个字符串的内容复制10次
print(10 * x)

print('北京' in y)
print('上海' in y)
