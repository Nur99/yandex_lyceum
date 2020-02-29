from PIL import Image


def twist_image(input_ﬁle_name, output_ﬁle_name):
    im = Image.open(input_ﬁle_name)
    x, y = im.size
    img = Image.new('RGB', (x, y))
    im2 = im.crop((0, 0, x // 2, y))
    im3 = im.crop((x // 2, 0, x, y))
    img.paste(im3, (0, 0))
    img.paste(im2, (x // 2, 0))
    img.save(output_ﬁle_name)
