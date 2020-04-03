class MinMaxWordFinder:
    def __init__(self):
        self.short_words = []
        self.min_len = None
        self.long_words = set()
        self.max_len = None

    def add_sentence(self, sentence):
        for word in sentence.split():
            if self.min_len is None:
                self.min_len = len(word)
                self.short_words.append(word)
            elif len(word) == self.min_len:
                self.short_words.append(word)
            elif len(word) < self.min_len:
                self.min_len = len(word)
                self.short_words = [word]
            if self.max_len is None:
                self.max_len = len(word)
                self.long_words.add(word)
            elif len(word) == self.max_len:
                self.long_words.add(word)
            elif len(word) > self.max_len:
                self.max_len = len(word)
                self.long_words = set((word,))

    def shortest_words(self):
        self.short_words.sort()
        return self.short_words

    def longest_words(self):
        return list(sorted(self.long_words))
