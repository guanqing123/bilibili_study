def copy(src, dest):
    origin = open(src, 'r', encoding='utf-8')
    s = origin.read()
    target = open(dest, 'w', encoding='utf-8')
    target.write(s)

    target.close()
    origin.close()


if __name__ == '__main__':
    copy('d.txt', 'e.txt')
