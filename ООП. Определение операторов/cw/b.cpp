class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, index):
        return self.lst[len(self.lst) - 1 - index]

    def __len__(self):
        return len(self.lst)

