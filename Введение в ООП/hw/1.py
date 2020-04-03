class BigBell:
    def __init__(self):
        self.state = 1

    def sound(self):
        if self.state:
            print('ding')
        else:
            print('dong')
        self.state ^= 1
