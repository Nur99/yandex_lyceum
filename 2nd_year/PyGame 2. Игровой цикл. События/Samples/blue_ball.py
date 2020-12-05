import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Синий круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    fps = 60
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
