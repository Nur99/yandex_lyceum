import math

from PIL import ImageDraw, Image


class MyImageDraw(ImageDraw.ImageDraw):
    def __init__(self, im, mode=None):
        super().__init__(im, mode=None)


    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        one_segment = math.pi * 2 / sides
        points = [
            (math.sin(one_segment * i + rotation) * radius,
             math.cos(one_segment * i + rotation) * radius)
            for i in range(sides)]
        points = [(val[0] + center_coords[0], val[1] + center_coords[1]) for val in points]
        self.polygon(points, fill, outline)


# im = Image.new('RGB', (800, 600))
# draw = MyImageDraw(im)
# draw.circle((200, 200), 50, fill='#00FFFF', outline="#FF00FF", width=5)
# draw.regular_polygon((400, 400), 5, 100, fill='#FF00FF', outline='#00FFFF')
# im.save('res.jpg')
