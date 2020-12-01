import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Желтый круг')
running = True
# Красим фон
screen.fill(pygame.Color('blue'))
circle_width = 0
circle_radius = 0
circle_exists = False  # переменная указывает на существование круга
circle_color = pygame.Color('yellow')
plus_radius = pygame.USEREVENT + 25  # номер нашего созданного события
# таймер вызова события увеличения радиуса круга
pygame.time.set_timer(plus_radius, 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # реакция на нажатие мыши
        if event.type == pygame.MOUSEBUTTONUP:
            circle_exists = True
            # красим фон и поверх него рисуем новый круг
            screen.fill(pygame.Color('blue'))
            circle_radius = 0
            circle_pos = event.pos
            pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
            # Событие увеличения радиуса круга
        if event.type == plus_radius and circle_exists:
            circle_radius += 1
            pygame.draw.circle(screen, circle_color, circle_pos, circle_radius, circle_width)
    pygame.display.flip()
    clock.tick(50)
pygame.quit()
