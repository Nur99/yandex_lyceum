import pygame

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    size = (100, 10)

    def __init__(self, pos):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        # добавляем в группу платформ
        self.add(platforms)
        self.image = pygame.Surface(Platform.size)
        self.image.fill(pygame.Color("gray"))
        self.rect = (pos, Platform.size)


class Ladder(pygame.sprite.Sprite):
    size = (10, 100)

    def __init__(self, pos):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        # добавляем в группу платформ
        self.add(ladders)
        self.image = pygame.Surface(Ladder.size)
        self.image.fill(pygame.Color("red"))
        self.rect = (pos, Ladder.size)


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color("blue"))
        self.rect = pygame.Rect(pos, (20, 20))

    def update(self):
        if pygame.sprite.spritecollideany(self, platforms) is None and pygame.sprite.spritecollideany(self,
                                                                                                      ladders) is None:
            self.rect.top += 1


# группа, содержащая все спрайты
all_sprites = pygame.sprite.Group()

# группа, содержащая все платформы
platforms = pygame.sprite.Group()

# группа, содержащая все лесенки
ladders = pygame.sprite.Group()

hero = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    Ladder(event.pos)
                else:
                    Platform(event.pos)
            if event.button == 3:
                if hero is None:
                    hero = Hero(event.pos)
                else:
                    hero.rect.topleft = event.pos
                    # если персонаж создан
        if hero is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hero.rect.left -= 10
                if event.key == pygame.K_RIGHT:
                    hero.rect.left += 10
                if pygame.sprite.spritecollideany(hero, ladders) is not None:
                    if event.key == pygame.K_UP:
                        hero.rect.top -= 10
                    if event.key == pygame.K_DOWN:
                        hero.rect.bottom += 10

    screen.fill(pygame.Color(0, 0, 0))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
