x = True
print(x)
print(type(x))  # <class 'bool'>
print(x + 10)  # 11  -> 1+10
print(False + 10)  # 10 -> 0+10
print('----------------------')
print(bool(18))  # 测试一下整数18的布尔值 True
print(bool(0), bool(0.0))  # False
# 总结,非0的整数的布尔值都是True
print(bool('北京欢迎你'))  # True
print(bool(''))  # False
# 所有非空字符串的布尔值都是True
print(bool(False))  # False
print(bool(None))  # False

'''
布尔值为False的情况
    False或者是None
    数值中的0,包含0, 0.0, 虚数0
    空序列,包含空字符串、空元组、空列表、空字典、空集合
    自定义对象的实例,该对象的__bool__()方法返回False或__len__()方法返回0
'''