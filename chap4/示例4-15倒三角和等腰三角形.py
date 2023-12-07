# 倒三角
for i in range(1, 6):
    for j in range(i, 6):
        print('*', end='')
    print()

print('-' * 20)

'''
&&&&*
&&&***
&&*****
&*******
*********
'''
# 等腰三角
for i in range(1, 6):
    for k in range(1, 6-i):
        print(' ', end='')

    for j in range(1, 2*i):
        print('*', end='')
    print()

'''
&&&*   1   1
&&***  3   2
&***** 5   3
*******7   4
&***** 5   5
&&***  3   6
&&&*   1   7
'''

#菱形
