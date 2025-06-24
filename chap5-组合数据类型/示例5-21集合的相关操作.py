"""
集合的方法        描述说明
s.add(x)        如果 x 不在集合 s 中，则将 x 添加到集合 s
s.remove(x)     如果 x 在集合中，将其删除，如果不在集合中，程序报错
s.clear()       清除集合中所有元素
"""
s = {10, 20, 30}
# 向集合中添加元素
s.add(100)
print(s)  # {100, 10, 20, 30}
# 删除元素
s.remove(20)
print(s)  # {100, 10, 30}
# 清空集合中所有元素
# s.clear()
# print(s)  # set()

# 集合的遍历操作
for item in s:
    print(item)

# 使用enumerate()函数
for index, item in enumerate(s):
    print(index, '-->', item)

# 集合的生成式
s = {i for i in range(1, 10)}
print(s)

s = {i for i in range(1, 10) if i % 2 == 1}
print(s)
