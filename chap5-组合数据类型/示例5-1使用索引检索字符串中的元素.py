# 序列是一个用于存储多个值的连续空间，每个值都对应一个整数的编号，称为索引

# 正向递增 索引
# range(start, stop[, step]) -> range object
# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step
s = 'helloworld'
for i in range(0, len(s)):
    print(i, s[i], end='\t\t')
print()
print('-'*40)

# 反向递减 索引
for i in range(-len(s), 0):
    print(i, s[i], end='\t\t')
print()
