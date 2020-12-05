import pygame

pygame.init()
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Слежу за тобой')
running = True

number = 0
# задаем цвет текста
text_color = pygame.Color('red')

# Выбрам шрифт для использования
# Стандартный шрифт, размером в 10
text_size = 100
font = pygame.font.Font(None, text_size)

while running:
    # красим фон
    screen.fill(pygame.Color('black'))
    # делаем изображение из текста
    text = font.render(str(number), True, text_color)
    # получаем размер получившейгося изображения
    (text_width, text_height) = text.get_rect().size
    # определяем координаты текста
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    # выводим наш текст
    screen.blit(text, [text_x, text_y])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # событие окна
        if event.type == pygame.WINDOWEVENT:
            # событие сворачивания окна
            if event.event == pygame.WINDOWEVENT_MINIMIZED:
                # считаем количество сворачиваний
                number += 1

    pygame.display.flip()
    clock.tick(50)
pygame.quit()
