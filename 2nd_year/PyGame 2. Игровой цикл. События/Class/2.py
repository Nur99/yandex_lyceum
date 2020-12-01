import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Шарики')
running = True
# параметра круга

circle_radius = 10
circle_color = pygame.Color('white')
# Пустые списки для координат и скоростей наших кругов
circle = []
speed = []
# Создаем второй холст
screen2 = pygame.Surface(screen.get_size())
# Запускаем окно
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(screen.get_size())
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            # Сохраняем полученные координаты
            circle.append(list(event.pos))
            speed.append([-1, -1])

    # Чистим второй холст
    screen2.fill(pygame.Color('black'))
    # Перерисовываем круги
    for i in range(len(circle)):
        # Проверяем на столкновение со стенками
        for ext in (0, 1):
            if circle[i][ext] >= size[ext] - circle_radius or circle[i][ext] <= circle_radius:
                speed[i][ext] = -speed[i][ext]
            # Изменяем координаты
            circle[i][ext] += speed[i][ext]
        # Рисуем круг
        pygame.draw.circle(screen2, circle_color, circle[i], circle_radius, 0)

    # Рисуем на экране сохраненное на втором холсте
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    clock.tick(100)
pygame.quit()
