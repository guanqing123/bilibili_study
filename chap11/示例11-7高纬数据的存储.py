import json

# 准备高纬数据
lst = [
    {'name': '杨淑娟', 'age': 18, 'score': 90},
    {'name': '陈梅梅', 'age': 21, 'score': 99},
    {'name': '张一一', 'age': 19, 'score': 89}
]

s = json.dumps(lst, ensure_ascii=False, indent=4)  # ensure_ascii正常显示中文,indent增加数据的缩进,美观用的。JSON格式的字符串更具有可读性
print(type(s), s)  # 编码 list -->str, 列表中是字典

# 解码
lst2 = json.loads(s)
print(type(lst2), lst2)

# 编码到文件中
with open('student.txt', 'w') as file:
    json.dump(lst, file, ensure_ascii=False, indent=4)

# 解码到程序
with open('student.txt', 'r') as file:
    lst = json.load(file)  # 直接是列表类型
    print(type(lst), lst)
