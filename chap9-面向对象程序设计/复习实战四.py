class Car(object):
    def __init__(self, chexing, chepai):
        self.chexing = chexing
        self.chepai = chepai

    def start(self):
        print('%s启动了' % self.chexing)

    def stop(self):
        print('%s停止了' % self.chexing)

class taxi(Car):
    def __init__(self, chexing, chepai, company):
        super().__init__(chexing, chepai)
        self.company = company

class jyjc(Car):
    def __init__(self, chexing, chepai, owner):
        super().__init__(chexing, chepai)
        self.owner = owner
