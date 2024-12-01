"""
元组生成式的结果是一个生成器对象，需要转换成元组或列表才能查看到元素内容

生成器对象中的元素可以使用 __next__() 方法进行获取
"""
t = (i for i in range(1, 4))
print(t)
# t=tuple(t)
# print(t)
# 遍历
# for item in t:
#     print(item)
print(t.__next__())
print(t.__next__())
print(t.__next__())

t = tuple(t)
print(t)
