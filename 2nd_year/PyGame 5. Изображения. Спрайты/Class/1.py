import os
import pygame


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


def main():
    size = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор мыши')

    # группа, содержащая все спрайты
    all_sprites = pygame.sprite.Group()

    # изображение должно лежать в папке data
    cursor_image = load_image("arrow.png")
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()

    # скрываем системный курсор
    pygame.mouse.set_visible(False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                # изменяем положение спрайта-стрелки
                cursor.rect.topleft = event.pos
        screen.fill(pygame.Color("black"))
        # рисуем курсор только если он в пределах окна
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
