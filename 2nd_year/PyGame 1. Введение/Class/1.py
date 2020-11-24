import pygame

pygame.init()
# Считываем размер окна
size = width, height = [int(i) for i in input().split()]
screen = pygame.display.set_mode(size)
screen.fill('red')


def draw():
    # # Задаем параметры линий
    # lines_color = (255, 255, 255)
    # lines_width = 5
    # # Рисуем главную диагональ
    # lines_points = [(0, 0), (width, height)]
    # pygame.draw.line(screen, lines_color, *lines_points, lines_width)
    # # Рисуем побочную диагональ
    # lines_points = [(0, height), (width, 0)]
    # pygame.draw.line(screen, lines_color, *lines_points, lines_width)
    pass


draw()

while pygame.event.wait().type != pygame.QUIT:
    # Обновляем изображение в окне
    pygame.display.flip()

pygame.quit()
