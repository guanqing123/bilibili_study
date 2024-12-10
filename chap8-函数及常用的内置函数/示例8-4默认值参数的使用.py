"""
默认值参数:
是在函数定义时，直接对形式参数进行赋值，在调用时如果该参数不传值，将使用默认值，如果该参数传值，则使用传递的值
"""
def happy_birthday(name='娟子姐',age=18):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

# 调用
happy_birthday() # 不用传参
happy_birthday('陈梅梅') # 位置传参
happy_birthday(age=19) # 关键字传参,name采用默认值

#happy_birthday(19) # 19会被赋值给哪个变量呢 ，如果使用位置传参的方式,19被传给了name

def fun(a,b=20): # a作为位置 参数,b默认值参数
    pass

def fun2(a=20,b): # 报错了，语法错误    ，当位置参数和默认值参数同时存在的时候，位置参数在后会被报错
    pass

#          当位置参数和关键字参数同时存在的时候 ,应该遵循 位置参数在前，默认值参数在后