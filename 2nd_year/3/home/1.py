class Point:
    def __init__(self, name, x, y):
        self.name = name
        self.coords = (x, y)

    def get_x(self):
        return self.coords[0]

    def get_y(self):
        return self.coords[1]

    def get_coords(self):
        return self.coords

    def __str__(self):
        return self.name + str(self.coords)

    def __invert__(self):
        return Point(self.name, self.get_y(), self.get_x())

    def __repr__(self):
        return "{}(\'{}\', {}, {})".format(self.__class__.__name__,
                                           self.name, self.get_x(), self.get_y())


if __name__ == "__main__":
    points = [Point('A', 0, 3), Point('B', 4, 0)]
    print(points)
    print(points[0])
    print(repr(points[0]))
