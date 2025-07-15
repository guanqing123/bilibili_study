# 导入
import random

# 设置随机数的种子
random.seed(10)
print(random.random())  # [0.0,1.0) 0.5714025946899135
print(random.random())  # 0.4288890546751146

print('-' * 40)
random.seed(10)
print(random.randint(1, 100))  # [1,100] 74

print('-' * 40)
for i in range(10):  # [m,n)步长为k,m->start,n->stop,k->step
    print(random.randrange(1, 10, 3))  # 12行代码执行了10次

print(random.uniform(1, 100))  # [data,b]随机小数 81.25126013057475

lst = [i for i in range(1, 11)]
print(random.choice(lst))  # lst是列表,称为序列 随机返回一个元素

# 随机的排序
random.shuffle(lst)
print(lst)  # [5, 4, 10, 7, 3, 2, 1, 6, 8, 9]

random.shuffle(lst)
print(lst)  # [3, 4, 5, 6, 8, 10, 7, 1, 2, 9]
