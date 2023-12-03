num = eval(input('请输入一个四位数：'))
print('个位上的数：', num % 10)
print('十位上的数：', num // 10 % 10)
print('百位上的数：', num // 100 % 10)
print('千位上的数：', num // 1000 % 10)

print('-' * 20)
num = input('请输入一个四位数：')  # num是字符串
print('个位上的数：', num[3])
print('十位上的数：', num[2])
print('百位上的数：', num[1])
print('千位上的数：', num[0])
