import os.path

# /Users/guanqing/python/bilibili_study/chap11-文件及IO操作/with.txt
print('获取目录或文件的绝对路径：', os.path.abspath('./with.txt'))
print('判断文件在磁盘上是否存在:', os.path.exists('with.txt'))  # 相对路径 True
print('判断文件在磁盘上是否存在:', os.path.exists('newwith.txt'))  # False
print('判断目录在磁盘上是否存在:', os.path.exists('data'))  # True

# 拼接路径： /Users/guanqing/python/bilibili_study/chap11-文件及IO操作/with.txt
print('拼接路径：', os.path.join('/Users/guanqing/python/bilibili_study/chap11-文件及IO操作', 'with.txt'))
print('分割文件名和文件后缀名：', os.path.splitext('with.txt'))  # 元组类型 ('with', '.txt')
# with.txt
print('提取文件名：', os.path.basename('/Users/guanqing/python/bilibili_study/chap11-文件及IO操作/with.txt'))
# /Users/guanqing/python/bilibili_study/chap11-文件及IO操作
print('提取路径：', os.path.dirname('/Users/guanqing/python/bilibili_study/chap11-文件及IO操作/with.txt'))
# True
print('判断是否有效路径：', os.path.isdir('/Users/guanqing/python/bilibili_study/chap11-文件及IO操作'))
# True
print('判断是否有效文件：', os.path.isfile('/Users/guanqing/python/bilibili_study/chap11-文件及IO操作/with.txt'))
