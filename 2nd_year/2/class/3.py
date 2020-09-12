PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, x, is_long=False):
        self.m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.n = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
        if x in self.m:
            if is_long:
                self.nt = self.n[self.m.index(x)]
            else:
                self.nt = x
                
    def __str__(self):
        return (self.nt)


class LoudNote(Note):
    def __str__(self):
        return (self.nt.upper())


class DefaultNote(Note):
    def __init__(self, x="до", is_long=False):
        self.m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.n = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
        if x in self.m:
            if is_long:
                self.nt = self.n[self.m.index(x)]
            else:
                self.nt = x


class NoteWithOctave(Note):
    def __init__(self, x, y, is_long=False):
        self.m = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
        self.n = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
        if x in self.m:
            if is_long:
                self.nt = self.n[self.m.index(x)]
            else:
                self.nt = x
            self.ny = y

    def __str__(self):
        w = self.nt + " " + "(" + self.ny + ")"
        return str(w)
