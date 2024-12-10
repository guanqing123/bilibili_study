"""
位置参数:
    是指调用时的参数个数和顺序必须与定义的参数个数和顺序相同
"""


def happy_birthday(name, age):
    print('祝' + name + '生日快乐')
    print(str(age) + '岁生日快乐')


# 调用
# happy_birthday('娟子姐') # TypeError: happy_birthday() missing 1 required positional argument: 'age'
# happy_birthday(18,'娟子姐') # TypeError: can only concatenate str (not "int") to str
# 正确的调用方式
happy_birthday('娟子姐', 18)
