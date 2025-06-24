"""
字符串是 Python 中的不可变数据类型
方法名                  描述说明
str.lower()            将 str 字符串全部转成小写字母，结果为一个新的字符串
str.upper()            将 str 字符串全部转成大写字母，结果为一个新的字符串
str.split(sep=None)    把 str 按照指定的分隔符 sep 进行分隔，结果为列表类型
str.count(sub)         结果为 sub 这个字符串在 str 中出现的次数
str.find(sub)          查询 sub 这个字符串在 str 中是否存在，如果不存在结果为 -1 ，如果存在，结果为 sub 首次出现的索引
str.index(sub)         功能与 find() 相同，区别在于要查询的子串 sub 不存在时，程序报错
str.startswith(s)      查询字符串 str 是否以子串 s 开头
str.endswith(s)        查询字符串 str 是否以子串 s 结束
"""
# 大小写转换
s1 = 'HelloWorld'
new_s2 = s1.lower()
print(s1, new_s2)  # HelloWorld helloworld

new_s3 = s1.upper()
print(s1, new_s3)  # HelloWorld HELLOWORLD

# 字符串的分隔
e_mail = 'ysj@126.com'
lst = e_mail.split('@')
print('邮箱名:', lst[0], '邮件服务器域名:', lst[1])  # 邮箱名: ysj 邮件服务器域名: 126.com

# 统计操作
print(s1.count('o'))  # o在字符串s1中出现了两次 2

# 检索操作
print(s1.find('o'))  # o在字符串s1中首次出现的位置 4
print(s1.find('p'))  # -1，没有找到
print(s1.index('o'))  # o在字符串s1中首次出现的位置 4
# print(s1.index('p')) # ValueError: substring not found 子串没有找到

# 判断前缀和后缀
print(s1.startswith('H'))  # True
print(s1.startswith('P'))  # False
print('demo.py'.endswith('.py'))  # True
print('text.txt'.endswith('.txt'))  # True
