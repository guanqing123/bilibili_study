"""
raise: 抛出一个异常，从而提醒程序出现了异常情况，程序能够正确地处理这些异常情况
raise 关键字的语法结构为：
    raise [Exception 类型 ( 异常描述信息 )]
"""
try:
    gender = input('请输入您的性别:')
    if gender != '男' and gender != '女':
        raise Exception('性别只能是男或女')
    else:
        print('您的性别是:', gender)
except Exception as e:
    print(e)