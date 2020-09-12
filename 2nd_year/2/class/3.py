PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]


class Note:
    def __init__(self, pitch, is_long=False):
        self.pitch = PITCHES.index(pitch)
        self.is_long = is_long

    def __str__(self):
        return LONG_PITCHES[self.pitch] if self.is_long else PITCHES[self.pitch]


class DefaultNote(Note):
    def __init__(self, pitch=PITCHES[0], is_long=False):
        super().__init__(pitch, is_long)


class LoudNote(Note):
    def __str__(self):
        return super().__str__().upper()


class NoteWithOctave(Note):
    def __init__(self, pitch, octave, is_long=False):
        self.octave = octave
        super().__init__(pitch, is_long)

    def __str__(self):
        return "{} ({})".format(super().__str__(), self.octave)

