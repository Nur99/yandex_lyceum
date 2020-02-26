from PIL import Image, ImageChops, ImageDraw


def gradient(mark):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    mark = mark.upper()
    for number in range(256):
        if mark == 'R':
            color = number, 0, 0
        elif mark == 'G':
            color = 0, number, 0
        else:
            color = 0, 0, number
        draw.line((number * 2, 0, number * 2, new_image.size[1]), fill=color, width=2)
    new_image.save('res.png', "PNG")
