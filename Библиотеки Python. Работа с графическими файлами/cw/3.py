from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x // 2):
        for j in range(y):
            pixels[i, j], pixels[x - i - 1, j] = pixels[x - i - 1, j], pixels[i, j]
    im.save('res.jpg')
