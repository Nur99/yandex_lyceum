import pygame

pygame.init()
pygame.display.set_caption('Zoom')
size = width, height = 501, 501
screen = pygame.display.set_mode(size)
running = True
with open('points.txt') as points:
    # разберем вводимые координаты. можно делать и без lambda-функций
    rects = list(map(lambda x: list(map(float, x[1:-1].replace(',', '.').split(';'))), points.read().split(', ')))

koef = 10
dkoef = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            koef += dkoef
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            koef -= dkoef if 0 < (koef - dkoef) else 0

    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, (255, 255, 255),
                        list(map(lambda x: [int(width // 2 + x[0] * koef), int(height // 2 - x[1] * koef)], rects)), 2)
    pygame.display.flip()
