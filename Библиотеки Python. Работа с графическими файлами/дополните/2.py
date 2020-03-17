from PIL import Image, ImageDraw

im = Image.new("RGBA", (450, 200), "pink")
drawer = ImageDraw.Draw(im)
drawer.line(((0, 200), (100, 0)), "green", 5)
drawer.rectangle(((100, 0), (160, 200)), "green")
drawer.line(((40, 120), (100, 120)), "green", 7)

for i in range(0, 200, 40):
    drawer.ellipse(((180, i), (220, i + 40)), "blue")
drawer.ellipse(((220, 160), (260, 200)), "blue")
for i in range(0, 200, 40):
    drawer.ellipse(((260, i), (300, i + 40)), "blue")

for i in range(0, 200, 40):
    drawer.ellipse(((180, i), (220, i + 40)), "blue")
drawer.ellipse(((220, 160), (260, 200)), "blue")
for i in range(0, 200, 40):
    drawer.ellipse(((260, i), (300, i + 40)), "blue")

drawer.line(((0, 200), (100, 0)), "green", 5)
drawer.rectangle(((100, 0), (160, 200)), "green")
drawer.line(((40, 120), (100, 120)), "green", 7)
im.save("name.png")
