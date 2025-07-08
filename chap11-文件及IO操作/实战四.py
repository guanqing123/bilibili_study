def get_auto_replay():
    autolst = []
    with open('replay.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        for item in lst:
            qa = item.split('|')
            qt = {'question': qa[0], 'answer': qa[1]}
            autolst.append(qt)
    return autolst


if __name__ == '__main__':
    lst = get_auto_replay()
    qi = input('请输入您要咨询问题:')
    flag = False
    for item in lst:
        if qi == item['question']:
            print(item['answer'])
            flag = True
            break
    if not flag:
        print('没有找到答案')
