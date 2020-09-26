from functools import total_ordering


@total_ordering
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

    def __lt__(self, other):
        return (self.name, self.coords) < (other.name, other.coords)

    def __le__(self, other):
        return (self.name, self.coords) <= (other.name, other.coords)

    def __eq__(self, other):
        return (self.name, self.coords) == (other.name, other.coords)


if __name__ == "__main__":
    p_A1 = Point('A', 1, 2)
    p_A2 = Point('A', 2, 1)
    p_B1 = Point('B', 2, 3)
    p_B2 = Point('B', 2, 3)
    print(p_A1 == p_A2, p_B1 == p_B2)
    print(p_A1 != p_A2, p_B1 != p_B2)
    print(p_A1 < p_A2, p_B1 > p_B2)
    print(p_A1 >= p_A2, p_B1 <= p_B2)
    print(max(p_A1, p_B2, p_A2, p_B2))
    print(min(p_A1, p_B2, p_A2, p_B2))

    points = [Point('A', 101, 1), Point('B', -1, 0),
              Point('A', 11, 0), Point('A', 111, -11)]
    points.sort()
    print(', '.join(map(str, points)))
