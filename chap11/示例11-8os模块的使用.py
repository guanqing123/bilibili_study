import os

print('当前的工作路径：', os.getcwd())
lst = os.listdir()
print('当前路径下的所有目录及文件：', lst)
print('指定路径下所有目录及文件：', os.listdir('/Users/guanqing'))
# 创建目录
# os.mkdir('好好学习') 如果要创建的文件夹存在程序报错 FileExistsError
# os.makedirs('./aa/bb/cc')
# 删除目录
# os.rmdir('./好好学习') # ./表示当前路径 FileNotFoundError, 如果要删除的目录不存在,程序会报错
# os.removedirs('./aa/bb/cc')

# 改变当前的工作路径
os.chdir('/Users/guanqing/python/bilibili_study')
print('当前的工作路径：', os.getcwd())  # 再写代码,工作路径就是：/Users/guanqing/python/bilibili_study

# 遍历目录树,相当于递归
for dirs, dirlst, filelst in os.walk('/Users/guanqing/python/bilibili_study/chap11'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('-' * 40)
