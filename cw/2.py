from PIL import Image

im = Image.open("image.jpg")
pixels = im.load()
x, y = im.size
pixels_count = x * y
R, G, B = 0, 0, 0

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        R += r
        G += g
        B += b

R, G, B = R // pixels_count, G // pixels_count, B // pixels_count
print(R, G, B)
