from PIL import Image, ImageDraw


def board(num, size):
    new_image = Image.new("RGB", (num * size, num * size), (0, 0, 0))
    draw = ImageDraw.Draw(new_image)
    for x_pos in range(num):
        for y_pos in range((x_pos + 1) % 2, num, 2):
            draw.rectangle((x_pos * size, y_pos * size, (x_pos + 1) * size - 1, (y_pos + 1) * size - 1),
                           fill=(255, 255, 255))
    new_image.save('res.png', "PNG")
