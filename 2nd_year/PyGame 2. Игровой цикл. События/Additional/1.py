import math
import pygame

size = width, height = 201, 201
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Вентилятор')
running = True
# задаем параметры круга
circle_color = polygon_color = pygame.Color('white')
circle_x = width // 2 + 1
circle_y = height // 2 + 1
circle_pos = (circle_x, circle_y)
circle_radius = 10
circle_width = 0
# задаем параметры лопастей
r = 70
speed = 0  # скорость вращения
polygon_width = 0
angle = 35 / 360
while running:
    # красим фон
    screen.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            # изменяем скорость в нужную сторону
            if event.button == 3:
                speed += 2 / 180
            elif event.button == 1:
                speed -= 2 / 180

    # рисуем круг
    circle_pos = (circle_x, circle_y)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)

    for i in range(3):
        # лопасть рисуется, как полигон по трем точкам
        point_1 = (circle_x + r * math.cos(angle * math.pi), circle_y + r * math.sin(angle * math.pi))
        point_2 = (
            circle_x + r * math.cos((angle + 1 / 6) * math.pi), circle_y + r * math.sin((angle + 1 / 6) * math.pi))
        polygon_points = [circle_pos, point_1, point_2]
        pygame.draw.polygon(screen, polygon_color, polygon_points, polygon_width)
        angle += 120 / 180

    # смещаем лопасти
    angle += speed

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
