import admin.my_admin as a  # 包名.模块名 admin是包名,my_admin是模块名
          #版权: 杨淑娟
          #讲师: ysj
a.info()  # 大家好,我叫ysj,今年18岁

print('-' * 40)
from admin import my_admin as b  # from 包名 import 模块 as 别名
b.info() #大家好,我叫ysj,今年18岁

print('-' * 40)
from admin.my_admin import info  # from 包名.模块名 import 函数/变量等
info() #大家好,我叫ysj,今年18岁

from admin.my_admin import *  # from 包名.模块名 import *
print(name) #杨淑娟
