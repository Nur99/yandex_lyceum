from PIL import Image, ImageDraw





def picture(file_name, width, height,

            sky_color=(135, 206, 235), ocean_color=(1, 123, 146),

            boat_color=(135, 69, 53), sail_color=(255, 255, 255),

            sun_color=(255, 207, 64)):

    im = Image.new("RGB", (width, height), sky_color)

    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)

    drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)

    drawer.rectangle(((int(width * 0.49), int(height * 0.3)), (int(width * 0.51), int(height * 0.65))), boat_color)

    drawer.polygon(((int(0.25 * width), int(height * 0.65)),

                    (int(0.75 * width), int(height * 0.65)),

                    (int(0.70 * width), int(height * 0.85)),

                    (int(0.30 * width), int(height * 0.85))),

                   boat_color)

    drawer.polygon(((int(0.51 * width), int(height * 0.3)),

                    (int(0.66 * width), int(height * 0.45)),

                    (int(0.51 * width), int(height * 0.60))),

                   sail_color)

    drawer.ellipse((

                   (int(0.8 * width), -int(0.2 * height)),

                   (int(1.2 * width), int(0.2 * height))),

                   sun_color)

    im.save("file_name.jpg")
