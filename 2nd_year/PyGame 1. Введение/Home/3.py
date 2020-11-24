import pygame

pygame.init()
size = width, height = (300, 200)
screen = pygame.display.set_mode(size)


def draw():
    # Устанавливаем параметры кирпичей и прослойки между ними
    rect_1_color = pygame.Color('red')
    rect_2_color = pygame.Color('white')
    rect_1_width = 0
    rect_2_width = 2
    rect_width = 30
    rect_height = 15
    # Номер ряда
    row_number = 0

    for i in range(0, width + 1, rect_width + rect_2_width):
        for j in range(0, height, rect_height + rect_2_width):
            # Координаты вершин ромба
            row_number += 1
            # В чётных рядах смещаем кирпичи
            if row_number % 2:
                rect_1_rect = [(i, j), (rect_width, rect_height)]
                rect_2_rect = [(i - rect_2_width, j - rect_2_width),
                               (rect_width + rect_2_width, rect_height + rect_2_width)]
            else:
                rect_1_rect = [(i - rect_width / 2, j), (rect_width, rect_height)]
                rect_2_rect = [(i - rect_width / 2 - rect_2_width, j - rect_2_width),
                               (rect_width + rect_2_width, rect_height + rect_2_width)]
            # Рисуем кирпич
            pygame.draw.rect(screen, rect_1_color, rect_1_rect, rect_1_width)
            # Рисуем белую обводку вокруг кирпича
            pygame.draw.rect(screen, rect_2_color, rect_2_rect, rect_2_width)


draw()

while pygame.event.wait().type != pygame.QUIT:
    # Обновляем изображение в окне
    pygame.display.flip()

pygame.quit()
