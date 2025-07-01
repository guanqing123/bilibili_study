class Circle():
    r = 0

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r * self.r

    def get_perimeter(self):
        return 2 * 3.14 * self.r


try:
    r = input('请输入圆的半径：')
    c = Circle(float(r))
    print(f'圆的面积是：{c.get_area()}')
    print(f'圆的周长是：{c.get_perimeter()}')
except:
    print('半径输入错误')
