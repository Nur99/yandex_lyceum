from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.__draw_map__ = draw_map
        self.__colors__ = dict(map(
            lambda x: (x, 'black'),
            set.union(*map(set, self.__draw_map__))
        ))
        self.__cell_size__ = cell_size

    def numbers(self):
        res = set()
        for row in self.__draw_map__:
            res |= set(row)
        return sorted(res)

    def set_color(self, number, color):
        self.__colors__[number] = color

    def set_cell_size(self, cell_size):
        self.__cell_size__ = cell_size

    def size(self):
        return tuple(map(
            lambda x: len(x) * self.__cell_size__,
            (
                self.__draw_map__[0],
                self.__draw_map__
            )
        ))

    def draw(self):
        img = Image.new('RGB', self.size(), 'black')
        draw = ImageDraw.Draw(img)
        for j, row in enumerate(self.__draw_map__):
            for i, cell in enumerate(row):
                x, y = map(lambda k: k * self.__cell_size__, (i, j))
                draw.rectangle(
                    (x, y, x + self.__cell_size__, y + self.__cell_size__),
                    fill=self.__colors__[cell]
                )
        return img


if __name__ == '__main__':
    draw_map = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    dr = Drawer(draw_map, 10)
    colors = {
        1: 'black',
        2: 'red',
        3: 'orange',
        4: 'yellow',
        5: 'green',
        6: 'lightblue',
        7: 'blue',
        8: 'violet',
        9: 'white'
    }
    for number, color in colors.items():
        dr.set_color(number, color)
    dr.draw().save('res.png')
