import os
# 删除文件
# os.remove('./data.txt') # 如果要删除的文件不存在,程序报错 FileNotFoundError
# 重命名
# os.rename('./with.txt', './newwith.txt')
# os.rename('./newwith.txt', './with.txt')

# 转换时间格式
import time


def date_format(longtime):
    s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))
    return s


# 获取文件信息
info = os.stat('./with.txt')
# <class 'os.stat_result'> os.stat_result(st_mode=33188, st_ino=39341910, st_dev=16777233, st_nlink=1, st_uid=501, st_gid=20, st_size=252, st_atime=1731285750, st_mtime=1731229436, st_ctime=1731245514)
print(type(info), info)
# 最近一次访问时间： 2024-11-11 08:42:30 1731285750.758722
print('最近一次访问时间：', date_format(info.st_atime), info.st_atime)
# 在操作系统中显示的文件的创建时间： 2024-11-10 21:31:54 1731245514.5585337
print('在操作系统中显示的文件的创建时间：', date_format(info.st_ctime), info.st_ctime)
# 最后一次修改时间： 2024-11-10 17:03:56 1731229436.488184
print('最后一次修改时间：', date_format(info.st_mtime), info.st_mtime)
print('文件的大小：', info.st_size) # 252

# 启动路径下的文件
# os.startfile('calc.exe')
import subprocess

# AppleScript command to open Calculator app
osascript_command = 'tell application "Calculator" to activate'

# Run the AppleScript command
subprocess.run(['osascript', '-e', osascript_command])

# 启动Python解释器
# os.startfile(r'C:\Users\...\Python312\python.exe')
