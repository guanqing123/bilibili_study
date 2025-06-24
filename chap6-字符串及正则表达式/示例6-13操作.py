import re

pattern = r'13[4-9]\d{8}'
lst = ['13809876543', '15109876543', '13278965439', '15912345665', '13198765432']
for item in lst:
    match = re.match(pattern, item)
    if match is not None:
        print(match.group())  # 13809876543

pattern = r'ysj_\w+'
s = 'ysj_python ysj_spider'
match = re.search(pattern, s)  # 它只会匹配到第一个符合条件的子串，而不会返回所有匹配的结果
print(match.group())  # ysj_python

match = re.findall(pattern, s)
print(match)  # 输出：['ysj_python', 'ysj_spider']
print(' '.join(match))  # 输出：ysj_python ysj_spider

'''
解析：
    \s*：匹配0个或多个空白字符（如空格、制表符）。
    @：匹配**@符号**。
    
    根据 \s*@ 进行分割：
    第一个 @ 符号前是空的，所以产生了一个空字符串 ''。
    第一个 @ 后分割出的部分是 '杨淑娟'。
    第二个 @ 后分割出的部分是 '刘梅梅'。
    第三个 @ 后分割出的部分是 '郭小川'
'''
pattern = r'\s*@'
s = '@杨淑娟 @刘梅梅 @郭小川'
lst = re.split(pattern, s)
print(lst)  # ['', '杨淑娟', '刘梅梅', '郭小川']
