lst = ['京A8888', '津B66666', '吉A77766']
for item in lst:
    area = item[:1]
    print(item, '归属地为:', area)
print('*' * 20)

for i in range(len(lst)):
    area = lst[i][:1]
    print(lst[i], '归属地为:', area)

print('*' * 20)

for index, item in enumerate(lst):
    area = item[:1]
    print(item, '归属地为:', area)
