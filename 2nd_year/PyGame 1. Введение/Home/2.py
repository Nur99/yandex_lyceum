import pygame

# Вводим количество ромбиков
n = int(input())
pygame.init()
size = width, height = (400, 300)
screen = pygame.display.set_mode(size)


def draw():
    # Устанавливаем жёлтый цвет фона
    screen.fill(pygame.Color('yellow'))

    polygon_width = 0
    polygon_color = pygame.Color('orange')
    # Шаг пригодится для определения координат вершин ромба
    step = n // 2
    # в цикле рисуем ромбики по одному
    for i in range(0, width - n + 1, n):
        for j in range(0, height - n + 1, n):
            # Координаты вершин ромба
            polygon_points = [(i, j + step), (i + step, j + 2 * step), (i + 2 * step, j + step), (i + step, j)]
            pygame.draw.polygon(screen, polygon_color, polygon_points, polygon_width)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
