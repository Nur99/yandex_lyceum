import pygame


# Кольца рисуем как круги с наслаиванием друг на друга
def draw(circle_width, number):
    circle_radius = circle_width * number
    circle_pos = (circle_radius, circle_radius)
    while number > 0:
        # Отрисовываем круг
        pygame.draw.circle(screen, colors[number % 3], circle_pos, circle_radius, 0)
        # Уменьшаем радиус
        circle_radius -= circle_width
        # Смещаем коэффициент цвета
        number -= 1


pygame.init()
# Считываем количество колец и их толщину
circle_width, number = [int(i) for i in input().split()]
size = width, height = (2 * circle_width * number, 2 * circle_width * number)
screen = pygame.display.set_mode(size)

colors = {0: pygame.Color('blue'), 1: pygame.Color('red'), 2: pygame.Color('green')}
draw(circle_width, number)
while pygame.event.wait().type != pygame.QUIT:
    # Обновляем изображение в окне
    pygame.display.flip()
pass

pygame.quit()
