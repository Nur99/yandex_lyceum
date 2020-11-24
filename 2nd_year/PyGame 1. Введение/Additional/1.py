import pygame

pygame.init()
# считываем размер и оттенок
w, hue = [int(i) for i in input().split()]
size = (width, width) = (300, 300)
screen = pygame.display.set_mode(size)


def draw():
    # Задаем цвета
    rect_color, polygon_1_color, polygon_2_color = pygame.Color('black'), pygame.Color('black'), pygame.Color('black')
    rect_color.hsva = hue, 100, 75, 100
    polygon_1_color.hsva = hue, 100, 100, 100
    polygon_2_color.hsva = hue, 100, 50, 100
    # Рисуем переднюю сторону куба
    rect_width = 0
    rect_rect = ((round(width / 2 - w * 0.75), round(width / 2 - w * 0.25)), (w, w))
    pygame.draw.rect(screen, rect_color, rect_rect, rect_width)
    # Рисуем верхнюю сторону куба
    polygon_1_point = [(round(width / 2 - w * 0.75), round(width / 2 - w * 0.25)),
                       (round(width / 2 + w * 0.25), round(width / 2 - w * 0.25)),
                       (round(width / 2 + w * 0.75), round(width / 2 - w * 0.75)),
                       (round(width / 2 - w * 0.25), round(width / 2 - w * 0.75))]
    pygame.draw.polygon(screen, polygon_1_color, polygon_1_point, 0)
    # Рисуем боковую сторону куба
    polygon_2_point = [(round(width / 2 + w * 0.25), round(width / 2 - w * 0.25)),
                       (round(width / 2 + w * 0.25), round(width / 2 + w * 0.75)),
                       (round(width / 2 + w * 0.75), round(width / 2 + w * 0.25)),
                       (round(width / 2 + w * 0.75), round(width / 2 - w * 0.75))]
    pygame.draw.polygon(screen, polygon_2_color, polygon_2_point, 0)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
