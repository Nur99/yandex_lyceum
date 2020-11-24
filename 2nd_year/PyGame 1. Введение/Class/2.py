import pygame

pygame.init()

# Считываем размер окна
size = width, height = [int(i) for i in input().split()]
screen = pygame.display.set_mode(size)


def draw():
    # Задаем размер отступа от границ холста
    step = 1
    # Задаем параметры прямоугольника
    rect_color = pygame.Color('red')
    rect_width = 0
    rect_point = [(step, step), (width - step * 2, height - step * 2)]
    # Рисуем прямоугольник
    pygame.draw.rect(screen, rect_color, rect_point, rect_width)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
