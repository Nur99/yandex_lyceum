import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Графический редактор v0.0000001')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    # очищаем экран один раз в самом начале
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
        pygame.display.flip()
    pygame.quit()
