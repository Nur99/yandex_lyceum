import random
import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))
    # обновление экрана


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Ненастроенный телевизор')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0

    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        draw(screen)
        pygame.display.flip()
    pygame.quit()
