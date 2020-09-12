from PIL import Image


im = Image.open("image.bmp")
pixels = im.load()
x, y = im.size
d = x // 4
for i in range(1, 5):
    for j in range(1, 5):
        if (i != 4) or (j != 4):
            im.crop(((j - 1) * d, (i - 1) * d, j * d, i * d)).save("image" + str(i) + str(j) + ".bmp")
