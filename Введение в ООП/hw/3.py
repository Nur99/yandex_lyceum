class BoundingRectangle:
    def __init__(self):
        self.first = True
        self.max_x = 0
        self.min_x = 0
        self.max_y = 0
        self.min_y = 0

    def add_point(self, x, y):
        if self.first:
            self.first = False
            self.max_x = x
            self.min_x = x
            self.max_y = y
            self.min_y = y
        else:
            self.max_x = max(self.max_x, x)
            self.min_x = min(self.min_x, x)
            self.max_y = max(self.max_y, y)
            self.min_y = min(self.min_y, y)

    def left_x(self):
        return self.min_x

    def right_x(self):
        return self.max_x

    def top_y(self):
        return self.max_y

    def bottom_y(self):
        return self.min_y

    def width(self):
        return self.max_x - self.min_x

    def height(self):
        return self.max_y - self.min_y
