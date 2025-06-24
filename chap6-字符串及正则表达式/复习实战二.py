str = 'HelloPython,HelloJava,hellophp'

param = input('请输入要查找的字符串:')
num = str.lower().count(param.lower())
print(f'{param}在{str}中一共出现了{num}次')

print("{0}在{1}中一共出现了{2}次".format(param, str, num))
