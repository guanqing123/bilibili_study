class Instrument(object):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('{} is making sound'.format(self.name))


class Erhu(Instrument):
    def __int__(self, name):
        super().__init__(name)


class Piano(Instrument):
    def __init__(self, name):
        super().__init__(name)


class Violin(Instrument):
    def __init__(self, name):
        super().__init__(name)


def play(instrument):
    instrument.make_sound()


erhu = Erhu("二胡")
piano = Piano("钢琴")
violin = Violin("小提琴")
play(erhu)
play(piano)
play(violin)
