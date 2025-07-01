"""
运算符     特殊方法                        功能描述
+         __add__()                     执行加法运算
-         __sub__()                     执行减法运算
<,<=,==   __lt__(),__le__(),__eq__()    执行比较运算
>,>=,!=   __gt__(),__ge__(),__ne__()    执行比较运算
*,/       __mul__(),__truediv__()       执行乘法运算,非整除运算
%,//      __mod__(),__floordiv__()      执行取余运算,整除运算
**        __pow__()                     执行幂运算
"""

a = 10
b = 20
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
print(dir(a))  # Python中的一切皆对象
print(a + b)  # 执行加法运算 30
print(a.__add__(b)) # 30
print(a.__sub__(b))  # 执行减法运算 -10
print(f'{a}<{b}吗?', a.__lt__(b)) # True
print(f'{a}<={b}吗?', a.__le__(b)) # True
print(f'{a}=={b}吗?', a.__eq__(b)) # False
print('-' * 40)
print(f'{a}>{b}吗?', a.__gt__(b)) # False
print(f'{a}>={b}吗?', a.__ge__(b)) # False
print(f'{a}!={b}吗?', a.__ne__(b)) # True
print('-' * 40)
print(a.__mul__(b))  # 乘法 200
print(a.__truediv__(b))  # 除法 0.5
print(a.__mod__(b))  # 取余 10
print(a.__floordiv__(b))  # 整除 0
print(a.__pow__(2))  # 幂运算 100
