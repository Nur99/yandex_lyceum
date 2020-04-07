class Queue:
    def __init__(self, *values):
        self.data = []
        self.append(*values)
    
    def __push(self, value):
        self.data.append(str(value))
        
    def __str__(self):
        if self.data == []:
            return "[]"
        else:        
            return "[" + " -> ".join(self.data) + "]"
        
    def append(self, *values):
        for value in values:
            self.__push(value)
            
    def copy(self):
        return Queue(*self.data[:])
    
    def __eq__(self, other):
        return self.data == other.data
    
    def pop(self):
        if self.data == []:
            return None
        else:
            return self.data.pop(0)
    
    def next(self):
        new_Queue = self.copy()
        new_Queue.pop()
        return new_Queue
    
    def __add__(self, other):
        new_Queue = self.copy()
        c = other.copy()
        new_data = []
        elem = c.pop()
        while elem is not None:
            new_data.append(elem)
            elem = c.pop()
        new_Queue.append(*new_data)
        return new_Queue
    
    def extend(self, other):
        new_data = []
        c = other.copy()
        elem = c.pop()
        while elem is not None:
            new_data.append(elem)
            elem = c.pop()
        self.append(*new_data)
        
    def __rshift__(self, other):
        new_Queue = self.copy()
        for _ in range(other):
            new_Queue.pop()
        return new_Queue
    
    def __iadd__(self, other):
        self.extend(other)
        return self
    
    def __next__(self):
        return self.next()
