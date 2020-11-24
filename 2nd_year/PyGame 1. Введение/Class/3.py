import pygame

pygame.init()

# Считываем размер окна и количество клеток
width, number = [int(i) for i in input().split()]
if width % number != 0:
    print('Количество клеток не кратно размеру окна')
    exit()
size = width, width
screen = pygame.display.set_mode(size)


def draw():
    # Переменная cell_color используется для определения цвета квадрата
    cell_color = number % 2

    square_width = width // number
    # По очереди отрисовываем квадраты
    for i in range(0, width, square_width):
        for j in range(0, width, square_width):
            square_point = [(i, j), (square_width, square_width)]
            # Меняем цвет
            cell_color = (cell_color + 1) % 2
            if not cell_color:
                square_color = pygame.Color('black')
            else:
                square_color = pygame.Color('white')
            # Рисуем квадрат
            pygame.draw.rect(screen, square_color, square_point, 0)
        # Для чётного количества клеток, смещаем переменную счетчик
        if number % 2 == 0:
            cell_color += 1


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
