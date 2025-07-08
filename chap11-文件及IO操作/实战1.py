# 创建3000份文件,文件名格式化位 序号_物资类别_用户识别码组成
# 1）序号从0001到3000
# 2）物资类别包括：水果、烟酒、粮油、肉蛋、蔬菜
# 3）用户识别码为9位的随机十六进制数码
import os
import random


def get_file_names():
    filenames = []
    lst = ['水果', '烟酒', '粮油', '肉蛋', '蔬菜']

    for i in range(1, 3001):
        if i < 10:
            num = '000' + str(i)
        elif i < 100:
            num = '00' + str(i)
        elif i < 1000:
            num = '0' + str(i)
        else:
            num = str(i)

        # category = lst[random.randint(0, 4)]
        category = random.choice(lst)  # Choose a random element from a non-empty sequence
        code = ''.join([random.choice('0123456789ABCDEF') for _ in range(9)])
        filename = f'{num}_{category}_{code}.txt'
        filenames.append(filename)
    return filenames


def create_file(filename):
    with open(filename, 'w') as f:
        pass


if __name__ == '__main__':
    if not os.path.exists('data'):
        os.mkdir('data')
    paths = get_file_names()
    for path in paths:
        create_file(os.path.join('data', path))
