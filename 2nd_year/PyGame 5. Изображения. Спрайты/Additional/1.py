import os
import sys
import time

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Gameover(pygame.sprite.Sprite):

    def __init__(self, group, image):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = -600

    def update(self):
        if self.rect.left < 0:
            self.rect.left += 8


def main():
    size = 600, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game over')
    clock = pygame.time.Clock()

    # группа, содержащая все спрайты
    all_sprites = pygame.sprite.Group()

    _ = Gameover(all_sprites, load_image("gameover.png"))

    running = True
    time.sleep(5)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("blue"))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == '__main__':
    main()
