"""
切片操作的语法结构
序列 [start ： end ： step]
start 切片的开始索引(包含)
end 切片的结束索引(不包含)
step 切片的步长(默认为1)
"""

s = 'HelloWorld'
# 切片操作
s1 = s[0:5:2]  # 索引从0开始,到5结束(不包含5),步长为2
print(s1)
# 省略了开始位置, start默认从0开始
print(s[:5:1])
# 省略开始位置start, 省略步长step
print(s[:5:])
# 省略结束位置
print(s[0::1])  # stop,默认到序列的最后一个元素(包含最后一个元素)

print(s[5::])
print(s[5:])
print(s[::])

# 步长为负数
print(s[::-1])
print(s[::-2])
