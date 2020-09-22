N = 7 
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]  
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, x, is_long=False):
        global PITCHES, LONG_PITCHES
        self.d = PITCHES.index(x)
        self.isq = is_long
        if x in PITCHES:
            if is_long:
                self.nt = LONG_PITCHES[PITCHES.index(x)]
            else:
                self.nt = x
                
    def __str__(self):
        return (self.nt)

    def get_interval(self, relf):
        global INTERVALS
        return INTERVALS[abs(self.d - relf.d)]

    def __lt__(self, relf):
        return self.d < relf.d

    def __le__(self, relf):
        return self.d <= relf.d

    def __gt__(self, relf):
        return self.d > relf.d

    def __ge__(self, relf):
        return self.d >= relf.d

    def __eq__(self, relf):
        return self.d == relf.d

    def __ne__(self, relf):
        return self.d != relf.d

    def __lshift__(self, g):
        return Note(PITCHES[(self.d - g) % 7], self.isq)

    def __rshift__(self, g):
        return Note(PITCHES[(self.d + g) % 7], self.isq)


class LoudNote(Note):
    def __str__(self):
        return (self.nt.upper())


class DefaultNote(Note):
    def __init__(self, x="до", is_long=False):
        global PITCHES, LONG_PITCHES
        super().__init__(x, is_long)


class NoteWithOctave(Note):
    def __init__(self, x, y, is_long=False):
        global PITCHES, LONG_PITCHES
        super().__init__(x, is_long)
        self.ny = y

    def __str__(self):
        w = self.nt + " " + "(" + self.ny + ")"
        return str(w)


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
