"""
多分支结构语法结构

if 表达式 1:
    语句块 1
elif 表达式 2:
    语句块 2
elif 表达式 n:
    语句块 n
else:
    语句块 n+1
"""
score = eval(input('请输入您的成绩：'))
# 多分支机构
if score < 0 or score > 100:
    print('成绩有误')
elif 0 <= score < 60:
    print('E')
elif 60 <= score < 70:
    print('D')
elif 70 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
else:
    print('A')
