class Note:
    def __init__(self, sound, long=False):
        lon = {
            'до': 'до-о',
            'ре': 'ре-э',
            'ми': 'ми-и',
            'фа': 'фа-а',
            'соль': 'со-оль',
            'ля': 'ля-а',
            'си': 'си-и'
        }
        if long:
            self.sound = lon[sound]
        else:
            self.sound = sound

    def __str__(self):
        return self.sound

    def play(self):
        print(self.sound)
