from PIL import Image, ImageDraw

im = Image.new("RGBA", (450, 200), "green")
drawer = ImageDraw.Draw(im)
drawer.line(((0, 200), (100, 0)), "red", 5)
drawer.rectangle(((100, 0), (160, 200)), "yellow")
for i in range(0, 200, 40):
    drawer.ellipse(((180, i), (220, i + 40)), "blue")
for i in range(0, 200, 80):
    drawer.ellipse(((220, i), (260, i + 40)), "orange")
    drawer.ellipse(((260, i), (300, i + 40)), "red")
drawer.rectangle(((310, 0), (450, 200)), "gray")
drawer.rectangle(((320, 0), (350, 200)), "magenta")
drawer.arc(((250, 0), (450, 100)), -90, 90, "white", 15)
drawer.arc(((250, 100), (450, 200)), -90, 90, "green", 25)
im.save("name.png")
