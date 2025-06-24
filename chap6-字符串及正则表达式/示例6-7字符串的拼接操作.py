"""
字符串的拼接
1) 使用 str.join() 方法进行拼接字符串
2) 直接拼接
3) 使用格式化字符串进行拼接
"""
s1 = 'hello'
s2 = 'world'
# (1)使用+进行拼接
print(s1 + s2)  # helloworld

# (2)使用字符串的join()方法
# 使用空字符串进行拼接
print(' '.join([s1, s2]))  # hello world

# hello*world*python*java*php
print('*'.join(['hello', 'world', 'python', 'java', 'php']))
# hello你好world你好python你好java你好php
print('你好'.join(['hello', 'world', 'python', 'java', 'php']))

# (3) 直接拼接
print('hello''world')  # helloworld

# (4)使用格式化字符串进行拼接
print('%s%s' % (s1, s2))  # helloworld
print(f'{s1}{s2}')  # helloworld
print('{0}{1}'.format(s1, s2))  # helloworld
