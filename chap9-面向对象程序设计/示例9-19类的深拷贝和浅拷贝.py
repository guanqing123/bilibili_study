"""
变量的赋值: 只是形成两个变量,实际上还是指向同一个对象
浅拷贝: 拷贝时,对象包含的子对象内容不拷贝,因此,源对象与拷贝对象会引用同一个子对象
深拷贝: 使用copy模块的deepcopy函数,递归拷贝对象中包含的子对象,源对象和拷贝对象所有的子对象也不相同
"""


class CPU:
    pass


class Disk:
    pass


class Computer:
    # 计算机由CPU和硬盘
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()  # 创建了一个CPU对象
disk = Disk()  # 创建了一个硬盘对象

# 创建一个计算机对象
com = Computer(cpu, disk)
# 变量（对象）的赋值
com1 = com
# <__main__.Computer object at 0x1070d57c0> 子对象的内存地址 <__main__.CPU object at 0x1070d5640> <__main__.Disk object at 0x1070d5760>
print(com, '子对象的内存地址', com.cpu, com.disk)
# <__main__.Computer object at 0x1070d57c0> 子对象的内存地址 <__main__.CPU object at 0x1070d5640> <__main__.Disk object at 0x1070d5760>
print(com1, '子对象的内存地址', com1.cpu, com1.disk)
print()

# 类对象的浅拷贝
import copy

com2 = copy.copy(com)  # com2是新产生的对象, com2的子对象,cpu,disk不变
print('-' * 40)
# <__main__.Computer object at 0x1070d57c0> 子对象的内存地址 <__main__.CPU object at 0x1070d5640> <__main__.Disk object at 0x1070d5760>
print(com, '子对象的内存地址', com.cpu, com.disk)
# <__main__.Computer object at 0x1078972f0> 子对象的内存地址 <__main__.CPU object at 0x1070d5640> <__main__.Disk object at 0x1070d5760>
print(com2, '子对象的内存地址', com2.cpu, com2.disk)

com3 = copy.deepcopy(com)  # com3是新产生的对象, com3的子对象,cpu,disk也变了
print('-' * 40)
# <__main__.Computer object at 0x1070d57c0> 子对象的内存地址 <__main__.CPU object at 0x1070d5640> <__main__.Disk object at 0x1070d5760>
print(com, '子对象的内存地址', com.cpu, com.disk)
# <__main__.Computer object at 0x107897020> 子对象的内存地址 <__main__.CPU object at 0x107897bc0> <__main__.Disk object at 0x107897c80>
print(com3, '子对象的内存地址', com3.cpu, com3.disk)


def test(a, b):
    print('a=', a, 'b=', b)


def test(a, b, c='c'):
    if c == 'c':
        test(a, b)
    else:
        print(f'a={a},b={b},c={c}')


test('111', '222')
test('1', '2', '3')
