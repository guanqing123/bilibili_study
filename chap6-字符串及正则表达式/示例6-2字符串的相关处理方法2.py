"""
方法名                        描述说明
str.replace(old,news)        使用 news 替换字符串 s 中所有的 old 字符串，结果是一个新的字符串
str.center(width,fill-char)  字符串 str 在指定的宽度范围内居中，可以使用 fill-char 进行填充
str.join(iter)               在 iter 中的每个元素的后面都增加一个新的字符串 str
str.strip(chars)             从字符串中去掉左侧和右侧 chars 中列出的字符串
str.lstrip(chars)            从字符串中去掉左侧 chars 中列出的字符串
str.rstrip(chars)            从字符串中去掉右侧 chars 中列出的字符串
"""
s = 'HelloWorld'
# 字符串的替换
print(s.replace('o', '你好'))  # Hell你好W你好rld
new_s = s.replace('o', '你好', 1)  # 最后一个参数是替换次数，默认是全部替换
print(new_s)  # Hell你好World

# 字符串在指定的宽度范围内居中
print(s.center(20))                       #      HelloWorld
print(s.center(20, '*'))  # *****HelloWorld*****

# join
print('-'.join(['hello', 'world', 'hi'])) # hello-world-hi

# 去掉字符串左右的空格
s = '    Hello    World    '
print(s.strip())  #
print(s.lstrip())  # 去除字符串左侧的空格
print(s.rstrip())  # 去除字符串右侧的空格

# 去掉指定的字符
s3 = 'dl-Helloworld'
print(s3.strip('ld'))  # 与顺序无关 -Hellowor
print(s3.lstrip('ld')) # -Helloworld
print(s3.rstrip('dl')) # dl-Hellowor
