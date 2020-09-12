from PIL import Image

im = Image.open("image.png")
pixels = im.load()
x, y = im.size

min_x, min_y, max_x, max_y = 0, 0, x - 1, y - 1

for i in range(x):
    ok = False
    for j in range(1, y):
        if pixels[i, j] != pixels[i, j - 1]:
            ok = True
            min_x = i
            break
    if ok:
        break

for i in range(x - 1, -1, -1):
    ok = False
    for j in range(1, y):
        if pixels[i, j] != pixels[i, j - 1]:
            ok = True
            max_x = i
            break
    if ok:
        break

for j in range(y):
    ok = False
    for i in range(1, x):
        if pixels[i, j] != pixels[i - 1, j]:
            ok = True
            min_y = j
            break
    if ok:
        break

for j in range(y - 1, -1, -1):
    ok = False
    for i in range(1, x):
        if pixels[i, j] != pixels[i - 1, j]:
            ok = True
            max_y = j
            break
    if ok:
        break

im.crop((min_x, min_y, max_x + 1, max_y + 1)).save("res.png")
