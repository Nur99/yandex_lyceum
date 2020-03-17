from PIL import Image
 
 
def negative(source, res):
    source = Image.open(source) 
    result = Image.new('RGB', source.size) 
    for x in range(source.size[0]): 
        for y in range(source.size[1]): 
            r, g, b = source.getpixel((x, y)) 
            result.putpixel((x, y), (255 - r, 255 - g, 255 - b)) 
    result.save(res, "JPEG")
