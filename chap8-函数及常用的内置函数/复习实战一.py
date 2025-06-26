import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 100))

print(lst)
max = 0
for i in range(len(lst)-1):
    if max < lst[i]:
        max = lst[i]

print(f'lst里面的最大值为:{max}')


def get_max(lst):
    max = 0
    for i in range(len(lst)-1):
        if max < lst[i]:
            max = lst[i]
    return max

lst = [random.randint(1, 100) for _ in range(10)]
print(lst)
max = get_max(lst)
print(f'lst里面最大值为:{max}')
