import os
# 删除文件
# os.remove('./a.txt') # 如果要删除的文件不存在,程序报错 FileNotFoundError
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
print(type(info), info)
print('最近一次访问时间：', date_format(info.st_atime))
print('在操作系统中显示的文件的创建时间：', date_format(info.st_ctime))
print('最后一次修改时间：', date_format(info.st_mtime))
print('文件的大小：', info.st_size)

# 启动路径下的文件
# os.startfile('calc.exe')
import subprocess

# AppleScript command to open Calculator app
osascript_command = 'tell application "Calculator" to activate'

# Run the AppleScript command
subprocess.run(['osascript', '-e', osascript_command])

# 启动Python解释器
# os.startfile(r'C:\Users\...\Python312\python.exe')
