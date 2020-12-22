import os
import random
import sys

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


class Bomb(pygame.sprite.Sprite):
    image = None
    image_boom = None

    def __init__(self, *group, size=(500, 500)):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(*group)
        if Bomb.image is None:
            Bomb.image = load_image("bomb2.png")
            Bomb.image_boom = load_image("boom.png")
        self.image = Bomb.image
        width, height = size
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.image.get_rect().width)
        self.rect.y = random.randrange(height - self.image.get_rect().height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


def main():
    size = 500, 500
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Boom them all')

    # группа, содержащая все спрайты
    all_sprites = pygame.sprite.Group()

    for i in range(20):
        # нам уже не нужно даже имя объекта!
        Bomb(all_sprites, size=size)

    running = True
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill(pygame.Color("black"))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
