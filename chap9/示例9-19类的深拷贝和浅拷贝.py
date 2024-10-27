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
print(com, '子对象的内存地址', com.cpu, com.disk)
print(com1, '子对象的内存地址', com1.cpu, com1.disk)
print()

# 类对象的浅拷贝
import copy

com2 = copy.copy(com)  # com2是新产生的对象, com2的子对象,cpu,disk不变
print('-' * 40)
print(com, '子对象的内存地址', com.cpu, com.disk)
print(com2, '子对象的内存地址', com2.cpu, com2.disk)

com3 = copy.deepcopy(com)  # com3是新产生的对象, com3的子对象,cpu,disk也变了
print('-' * 40)
print(com, '子对象的内存地址', com.cpu, com.disk)
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
