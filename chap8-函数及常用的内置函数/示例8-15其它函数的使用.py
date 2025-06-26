"""
函数名称                        描述说明
format(value,format_spec)     将 value 以 format_spec 格式进行显示
len(s)                        获取 s 的长度或 s 元素的个数
id(obj)                       获取对象的内存地址
type(x)                       获取 x 的数据类型
eval(s)                       执 s 这个字符串所表示的 Python 代码
"""
# format()
# 数值型默认右对齐
print(format(3.14, '20'))       #                3.14
# 字符串默认左对齐
print(format('hello', '20'))    #hello
# <左对齐，*表示的填充符，20表示的是显示的宽度
print(format('hello', '*<20'))  #hello***************
print(format('hello', '*>20'))  #***************hello
print(format('hello', '*^20'))  #*******hello********

print(format(3.1415926, '.2f'))  # 3.14
print(format(20, 'b')) # 10100
print(format(20, 'o')) # 24
print(format(20, 'x')) # 14
print(format(20, 'X')) # 14

print('-' * 40)
print(len('helloworld')) # 10
print(len([10, 20, 30, 40, 50])) # 5

print('-' * 40)
print(id(10)) # 4392226600
print(id('helloworld')) # 4419676208
print(type('hello'), type(10)) # <class 'str'> <class 'int'>

print(eval('10+30')) # 40
print(eval('10>30')) # False
