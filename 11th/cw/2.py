from PIL import Image
import itertools


def transparency(filename1, filename2):
    im = Image.open(filename1)
    pixels = im.load()
    pixels2 = Image.open(filename2).load()
    x, y = im.size
    for i, j in itertools.product(range(x), range(y)):
        r, g, b = pixels[i, j]
        r2, g2, b2 = pixels2[i, j]
        pixels[i, j] = (
            int(.5 * r + 0.5 * r2),
            int(.5 * g + .5 * g2),
            int(.5 * b + 0.5 * b2),
        )
    im.save('res.jpg')
