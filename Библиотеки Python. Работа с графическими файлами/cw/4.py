from PIL import Image


def mirror():
    im = Image.open('image.jpg')
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(x - i):
            pixels[j, i], pixels[x - i - 1, x - j - 1] = pixels[x - i - 1, x - j - 1], pixels[j, i]
    im.save('res.jpg')
