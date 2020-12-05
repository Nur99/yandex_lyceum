import pygame

size = width, height = 501, 501
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('К щелчку')
running = True
# задаем параметры круга
circle_color = pygame.Color('red')
circle_x = x1 = width // 2 + 1
circle_y = y1 = height // 2 + 1
circle_pos = (circle_x, circle_y)
circle_radius = 20
circle_width = 0

while running:
    # красим фон
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Сохраняем координаты курсора
            x1, y1 = event.pos
    # если центр круга не совпадает с координатами полученными при нажатии кнопки мыши,
    # изменяем их в нужную сторону
    if x1 > circle_x:
        circle_x += 1
    elif x1 < circle_x:
        circle_x -= 1

    if y1 > circle_y:
        circle_y += 1
    elif y1 < circle_y:
        circle_y -= 1

    # рисуем круг
    circle_pos = (circle_x, circle_y)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
