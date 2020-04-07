class SparseArray:
    def __init__(self):
        self.dict_ = {}

    def __getitem__(self, index):
        return self.dict_.get(index, 0)

    def __setitem__(self, index, value):
        if value == 0 and value in self.dict_:
            self.dict_.pop(index)
        elif value == 0:
            pass
        else:
            self.dict_[index] = value

