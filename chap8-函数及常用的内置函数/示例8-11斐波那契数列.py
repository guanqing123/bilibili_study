"""
斐波那契数列（ Fibonacci sequence ），又称黄金分割线，是因数学家莱昂纳
多 · 斐波那契（ Leonardo Fibonacci ）以兔子繁殖为例子而引入，故又称为
“兔子数列”，指的是这样一个数列： 1 、 1 、 2 、 3 、 5 、 8 、 13 、 21 、
34 、......，从第三项开始，每项都等于前两项之和

公式为： f(n)=f(n-1)+f(n-2)
"""


def fac(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fac(n - 1) + fac(n - 2)


print(fac(9))  # 第9位上的数字

for i in range(1, 10):
    print(fac(i), end='\t')
print()
