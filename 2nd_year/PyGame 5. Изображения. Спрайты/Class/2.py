import os

import pygame

size = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Герой двигается!')


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    dist = 10
    hero_image = load_image("creature.png", -1)

    def __init__(self, *args):
        super().__init__(*args)
        self.image = Hero.hero_image
        self.rect = self.image.get_rect()

    def update(self, *args, **kwargs):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.rect.top += self.dist
        elif key[pygame.K_UP]:
            self.rect.top -= self.dist
        if key[pygame.K_RIGHT]:
            self.rect.left += self.dist
        elif key[pygame.K_LEFT]:
            self.rect.left -= self.dist


def main():


    # группа, содержащая все спрайты
    all_sprites = pygame.sprite.Group()

    # изображение должно лежать в папке data
    hero = Hero(all_sprites)

    # шаг перемещения

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Проверяем нажатые кнопки
            hero.update()

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
