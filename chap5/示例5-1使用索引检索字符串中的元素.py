# 正向递增
s = 'helloworld'
for i in range(0, len(s)):
    print(i, s[i], end='\t\t')
print()
print('-'*40)

# 反向递减
for i in range(-len(s), 0):
    print(i, s[i], end='\t\t')
print()
