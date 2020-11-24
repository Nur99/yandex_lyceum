import pygame

pygame.init()

# Считываем количество эллипсов
number = int(input())
size = width, height = (300, 300)
screen = pygame.display.set_mode(size)


def draw():
    ellipse_color = pygame.Color('white')
    ellipse_width = 1

    # Определяем шаг
    step = (width // 2) // number
    for i in range(0, width // 2, step):
        # Рисуем эллипсы, вытянутые по высоте
        ellipse_rect = [(i, 0), (width - i * 2, width)]
        pygame.draw.ellipse(screen, ellipse_color, ellipse_rect, ellipse_width)
        # Рисуем эллипсы, вытянутые по ширине
        ellipse_rect = [(0, i), (width, width - i * 2)]
        pygame.draw.ellipse(screen, ellipse_color, ellipse_rect, ellipse_width)


draw()
while pygame.event.wait().type != pygame.QUIT:
    # Обновляем изображение в окне
    pygame.display.flip()

pygame.quit()
