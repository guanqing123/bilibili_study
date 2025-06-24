import re

pattern = '\d\.\d+'
s = 'I study Python3.11 every day Python2.7 I love you'
match = re.search(pattern, s)

s2 = '4.10 Python I study every day'
s3 = 'I study Python every day'

match2 = re.search(pattern, s2)
match3 = re.search(pattern, s3)  # None
print(match)  # <re.Match object; span=(14, 18), match='3.11'>
print(match2)  # <re.Match object; span=(0, 4), match='4.10'>
print(match3)  # None

print(match.group())  # 3.11
print(match2.group())  # 4.10
