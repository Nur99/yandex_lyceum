from PIL import Image
 

def make_preview(size, n_colors):
    im = Image.open("image.jpg")
    im2 = im.resize((size))
    im3 = im2.quantize(n_colors)
    im3.save('res.bmp')
