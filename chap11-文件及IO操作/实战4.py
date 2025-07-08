def find_answer(question):
    with open('replay.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            qa = line.split('|')
            if question == qa[0]:
                return qa[1]
    return False


if __name__ == '__main__':
    question = input('请输入问题：')
    while True:
        if question == 'bye':
            print('欢迎下次再来')
            break
        else:
            answer = find_answer(question)
            if not answer:
                question = input('您说的问题我不知道,您可以问我关于订单,物流等问题')
            else:
                print(answer)
                question = input('请输入问题：退出请输入bye')
