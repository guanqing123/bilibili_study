"""
格式化字符串的三种方式
1)占位符
%s : 字符串格式
%d : 十进制整数格式
%f : 浮点数格式
"""
# (1)使用占位符进行格式化
name = '马冬梅'
age = 18
score = 98.5
print('%s' % name)
print('姓名:%s,年龄:%d,成绩:%f' % (name, age, score))
print('姓名:%s,年龄:%d,成绩:%.1f' % (name, age, score))

"""
2)f-string
Python3.6 引入的格式化字符串的方式，比 {} 标明被替换的字符
"""
# (2)f-string
print('*'*20, 'f-string', '*'*20)
print(f'姓名:{name},年龄:{age},成绩:{score}')

"""
3)str.format() 方法
模板字符串 .format( 逗号分隔的参数 )
"""
print('*'*20, 'str.format()', '*'*20)
# (3)使用字符串的format方法
print('姓名:{0},年龄:{1},成绩:{2}'.format(name, age, score))
print('姓名:{2},年龄:{0},成绩:{1}'.format(age, score, name))
