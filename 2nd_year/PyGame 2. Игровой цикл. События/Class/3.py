import pygame

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Перетаскивание')
running = True
# задаем параметры квадрата
rect_width = 0
rect_x = 0
rect_y = 0
square_width = 100
rect_color = pygame.Color('green')
rect_rect = ((rect_x, rect_y), (square_width, square_width))
x1 = x2 = y1 = y2 = 0

while running:
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Сохраняем координаты курсора
            x1, y1 = event.pos
            # если курсор не попал в область квадрата, координаты обнуляем
            if (x1 < rect_x) or (x1 > rect_x + square_width) or (y1 < rect_y) or (y1 > rect_y + square_width):
                x1 = y1 = 0

        # реакция на отжатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            # Сохраняем новые координаты вершины квадрата
            rect_x += x2
            rect_y += y2
            # обнуляем смещение координат
            x1 = x2 = y1 = y2 = 0
        # реакция на движение мышки с условием того, что кнопка зажата
        if event.type == pygame.MOUSEMOTION and x1 > 0:
            # считаем смещение координат
            x2 = event.pos[0] - x1
            y2 = event.pos[1] - y1
    # рисуем прямоугольник
    rect_rect = ((rect_x + x2, rect_y + y2), (square_width, square_width))
    pygame.draw.rect(screen, rect_color, rect_rect, rect_width)

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
