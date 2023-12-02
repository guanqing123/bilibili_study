print('北京欢迎你' + '2023')
# print('北京欢迎你'+2023) TypeError: can only concatenate str (not "int") to str

a = 23
b = 24.5
c = "我要开始减肥了"
print(a, '\n', c, '\n', b, sep='', end='\n')

print('aaa', 'b', sep='&', end='\n')


def printL(self, *args):  # known special case of print
    print(self, *args, sep='&', end="", file=None)
    pass


printL('abc', 'def')
