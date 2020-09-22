class Melody():
    def __init__(self, m=[]):
        self.x = []
        for i in range(len(m)):
            self.x.append(m[i])

    def append(self, x):
        self.x.append(x)

    def replace_last(self, x):
        self.x[-1] = x

    def remove_last(self):
        del self.x[-1]

    def clear(self):
        self.x.clear()

    def __str__(self):
        s = ""
        for i in self.x:
            s += str(i) + ", "
        return s[:-2].capitalize()
    
    def __len__(self):
        return len(self.x)

    def __rshift__(self, g):
        k = []
        for i in self.x:
            if i.d + g < 7:
                k.append(i >> g)
            else:
                k = self.x
                break
        return Melody(k)

    def __lshift__(self, g):
        k = []
        for i in self.x:
            if i.d - g > -1:
                k.append(i << g)
            else:
                k = self.x
                break
        return Melody(k)
