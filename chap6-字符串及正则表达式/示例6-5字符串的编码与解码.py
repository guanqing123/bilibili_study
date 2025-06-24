"""
字符串的编码

将 str 类型转换成 bytes 类型，需要使用到字符串的 encode() 方法
语法格式：
str.encode(encoding=‘utf-8’, errors=‘strict/ignore/replace’)
"""
s = '伟大的中国梦'
# 编码 str->bytes
scode = s.encode(errors='replace')  # 默认是utf-8 ,因为utf-8中文占3个字节
print(scode)  # b'\xe4\xbc\x9f\xe5\xa4\xa7\xe7\x9a\x84\xe4\xb8\xad\xe5\x9b\xbd\xe6\xa2\xa6'

scode_gbk = s.encode('gbk', errors='replace')  # gbk中中文占2个字节
print(scode_gbk)  # b'\xce\xb0\xb4\xf3\xb5\xc4\xd6\xd0\xb9\xfa\xc3\xce'

# 编码中的出错问题
s2 = '耶✌'
scode_error = s2.encode('gbk', errors='replace')
print(scode_error)  # b'\xd2\xae?'
# UnicodeEncodeError: 'gbk' codec can't encode character '\u270c' in position 1: illegal multibyte sequence
# print(s2.encode('gbk', errors='strict'))

"""
字符串的解码

将 bytes 类型转换成 str 类型，需要使用到 bytes 类型的 decode() 方法
语法格式：
bytes.decode(encoding=‘utf-8’, errors=‘strict/ignore/replace’)
"""
# 解码过程bytes->str
print(bytes.decode(scode_gbk, 'gbk'))  # 伟大的中国梦
print(bytes.decode(scode, 'utf-8'))  # 伟大的中国梦
print(bytes.decode(scode_error, 'gbk'))  # 耶?
