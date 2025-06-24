"""
元组生成式的结果是一个生成器对象，需要转换成元组或列表才能查看到元素内容

生成器对象中的元素可以使用 __next__() 方法进行获取
"""
t = (i for i in range(1, 4))
print(t)  # 生成器对象 <generator object <genexpr> at 0x107d69600>
# t=tuple(t)
# print(t) #(1, 2, 3)
# 遍历
# for item in t:
#     print(item)
print(t.__next__())
print(t.__next__())
print(t.__next__())

t = tuple(t)
print(t)

"""
元组                                  列表
不可变序列                           可变序列
无法实现添加、删除和修改元素等操作       append() 、 insert() 、 remove() 、 pop() 等方法实现添加和删除列表元素
支持切片访问元素，不支持修改操作         支持切片访问和修改列表中的元素
访问和处理速度快                      访问和处理速度慢
可以作为字典的键                      不能作为字典的键
"""
