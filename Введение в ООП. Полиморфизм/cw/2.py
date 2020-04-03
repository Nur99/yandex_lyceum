class LeftParagraph:
    def __init__(self, text_width):
        self.text_width = text_width
        self.first_word = True
        self.words = []
        self.lines = []
        self.current_width = 0

    def add_word(self, word):
        addition = 1 if (self.current_width > 0) else 0
        if self.current_width + addition + len(word) <= self.text_width:
            self.words.append(word)
            self.current_width += len(word) + addition
        else:
            self.lines.append(' '.join(self.words))
            self.words = [word]
            self.current_width = len(word)

    def end(self):
        print(*self.lines, sep='\n')
        print(' '.join(self.words))
        self.words = []
        self.lines = []
        self.current_width = 0


class RightParagraph:
    def __init__(self, text_width):
        self.text_width = text_width
        self.first_word = True
        self.words = []
        self.current_width = 0
        self.lines = []

    def add_word(self, word):
        addition = 1 if (self.current_width > 0) else 0
        if self.current_width + addition + len(word) <= self.text_width:
            self.words.append(word)
            self.current_width += len(word) + addition
        else:
            line = ' '.join(self.words)
            space_prefix = ' ' * (self.text_width - len(line))
            self.lines.append(space_prefix + line)
            self.words = [word]
            self.current_width = len(word)

    def end(self):
        line = ' '.join(self.words)
        space_prefix = ' ' * (self.text_width - len(line))
        print(*self.lines, sep='\n')
        print(space_prefix + line)
        self.words = []
        self.lines = []
        self.current_width = 0
