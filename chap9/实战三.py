# 乐器类
class Instrument:
    def make_sound(self):
        pass


# 二胡
class Erhu(Instrument):
    def make_sound(self):
        print('二胡')


# 钢琴
class Piano(Instrument):
    def make_sound(self):
        print('钢琴')


# 小提琴
class Violin(Instrument):
    def make_sound(self):
        print('小提琴')


def play(obj):
    obj.make_sound()


erhu = Erhu()
piano = Piano()
violin = Violin()
play(erhu)
play(piano)
play(violin)
