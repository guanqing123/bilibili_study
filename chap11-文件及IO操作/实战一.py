# 创建3000份文件,文件名格式化位 序号_物资类别_用户识别码组成
# 1）序号从0001到3000
# 2）物资类别包括：水果、烟酒、粮油、肉蛋、蔬菜
# 3）用户识别码为9位的随机十六进制数码

import os
import random

for i in range(1, 3001):
    num = str(i).zfill(4)

    lst = ['水果', '烟酒', '粮油', '肉蛋', '蔬菜']
    category = lst[i % 5]

    # 用户识别码为9位的随机十六进制数码
    hex_code = ''.join(random.choice('0123456789ABCDEF') for _ in range(9))
    file_name = '{}_{}_{}.txt'.format(num, category, hex_code)
    # 把文件创建到 data 目录下
    if not os.path.exists('data'):
        os.mkdir('data')
    with open(os.path.join('data', file_name), 'w', encoding='utf-8') as file:
        pass
