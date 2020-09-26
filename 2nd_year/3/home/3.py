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

    def get_name(self):
        return self.name

    def get_coords(self):
        return self.coords

    def __str__(self):
        return self.name + str(self.coords)

    def __repr__(self):
        return "{}(\'{}\', {}, {})".format(self.__class__.__name__,
                                           self.name, self.get_x(), self.get_y())

    def __lt__(self, other):
        return self.coords < other.coords

    def __le__(self, other):
        return self.coords <= other.coords

    def __eq__(self, other):
        return self.coords == other.coords


class CheckMark:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def __bool__(self):
        x1, y1 = self.points[0].get_coords()
        x2, y2 = self.points[1].get_coords()
        x3, y3 = self.points[2].get_coords()
        return (x3 - x1) * (y2 - y1) != (x2 - x1) * (y3 - y1)

    def __str__(self):
        return ''.join(map(Point.get_name, self.points))

    def __eq__(self, other):
        return self.points[1] == other.points[1] and sorted(self.points[::2]) == sorted(other.points[::2])


if __name__ == "__main__":
    p_A = Point('A', 1, 2)
    p_B = Point('B', 0, 1)
    p_C = Point('C', -1, 2)
    p_D = Point('D', 2, 2)
    p_E = Point('E', 2, 0)
    p_F = Point('F', 2, -1)
    cm_ABC = CheckMark(p_A, p_B, p_C)
    cm_DEF = CheckMark(p_D, p_E, p_F)
    cm_ABB = CheckMark(p_A, p_B, p_B)
    print(cm_ABC, bool(cm_ABC))
    print(cm_DEF, bool(cm_DEF))
    print(cm_ABB, bool(cm_ABB))

    p_A = Point('A', 1, 2)
    p_B = Point('B', 0, 1)
    p_C = Point('C', -1, 2)
    p_D = Point('D', -1, 2)
    cm_ABC = CheckMark(p_A, p_B, p_C)
    cm_CBA = CheckMark(p_C, p_B, p_A)
    cm_ACB = CheckMark(p_A, p_C, p_B)
    cm_ABD = CheckMark(p_A, p_B, p_D)
    cm_DBA = CheckMark(p_D, p_B, p_A)
    print(cm_ABC == cm_CBA, cm_ABC == cm_ABD)
    print(cm_ABC == cm_DBA, cm_ABC == cm_ACB)
