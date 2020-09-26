class Point:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return (self.x, self.y)

    def __invert__(self):
        return Point(self.name, self.y, self.x)

    def __str__(self):
        return '{}({}, {})'.format(self.name, self.x, self.y)

    def __repr__(self):
        return 'Point(%r, %r, %r)' % (self.name, self.x, self.y)


class CheckMark(Point):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return self.a.name + self.b.name + self.c.name
    
    def __bool__(self):
        if self.a.x == self.b.x == self.c.x:
            return False
        elif self.a.y == self.b.y == self.c.y:
            return False
        elif self.a.x == self.b.x and self.a.y == self.b.y:
            return False
        elif self.b.x == self.c.x and self.b.y == self.c.y:
            return False
        elif self.a.x == self.c.x and self.a.y == self.c.y:
            return False
        elif self.a.x == self.a.y and self.b.x == self.b.y and self.c.x == self.c.y:
            return False
        elif self.a.x - self.b.x == self.b.x - self.c.x and self.a.y - self.b.y == self.b.y - self.c.y:
            return False
        return True

    def __eq__(self, other):
        if self.b.x == other.b.x and self.b.y == other.b.y:
            if self.a.x == other.a.x and self.a.y == other.a.y:
                if self.c.x == other.c.x and self.c.y == other.c.y:
                    
                    return True
            elif self.a.x == other.c.x and self.a.y == other.c.y:
                if self.c.x == other.a.x and self.c.y == other.a.y:
                    return True
        return False
    
