import jieba

# 读取进来
with open('华为手机.txt', 'r', encoding='utf-8') as file:
    s = file.read()
# print(s)
# 分词
lst = jieba.lcut(s)
print(lst)

# 去重操作
set1 = set(lst)  # 使用集合实现去重
d = {}  # key:词,value:出现的次数
for item in set1:
    if len(item) >= 2:  # 只保留长度大于2的词
        d[item] = 0

# print(d)
for item in lst:
    if item in d:  # 判断item作为 键 是否在字典中
        d[item] = d.get(item) + 1
# print(d)

# 将字典转换成列表
lst = list(d.items())
# [('手机', 47), ('华为', 46), ('用户', 28), ('方面', 19), ('技术', 15), ('产品', 13), ('通过', 11)]
# 排序 sorted会产生一个新的数组，不会改变原数组; 根据元组的第二个元素进行排序
nl = sorted(lst, key=lambda x: x[1], reverse=True)
# 列表排序,改变的是列表本身
lst.sort(key=lambda x: x[1], reverse=True)

new_lst = []
for item in d:
    new_lst.append([item, d[item]])
print(new_lst)

# 列表排序 key=lambda x: x[1] 表示按照每个子列表中的第二个元素（即词频）作为排序依
new_lst.sort(key=lambda x: x[1], reverse=True)
# [['手机', 47], ['华为', 46], ['用户', 28], ['方面', 19], ['技术', 15], ['产品', 13], ['通过', 11]]
print(new_lst[0:11])  # 显示的是前10项
