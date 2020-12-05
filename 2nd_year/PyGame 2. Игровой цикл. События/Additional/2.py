import pygame

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption('Прямоугольники с Ctrl+Z')
running = True
rect_color = pygame.Color('white')
# создаем пустые списки для парметров прямоугольников
start_x = []
start_y = []
rect_width = []
rect_height = []

x1, y1, x2, y2 = 0, 0, 0, 0

drawing = False  # режим рисования выключен
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # событие нажатия на кнопку клавиатуры
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                if event.mod & pygame.KMOD_LCTRL or event.mod & pygame.KMOD_RCTRL:
                    # Если одновременно зажаты Ctrl+Z и есть нарисованные прямоугольники
                    # тогда удаляем последний
                    start_x.pop()
                    start_y.pop()
                    rect_width.pop()
                    rect_height.pop()
        # событие нажатия на левую кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True  # включаем режим рисования
            x1, y1 = event.pos
            x2 = x1
            y2 = y1

        # событие отжатия левой кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False
            # добавляем данные о прямоугольнике в массивы
            start_x.append(x1)
            start_y.append(y1)
            rect_width.append(x2 - x1)
            rect_height.append(y2 - y1)
        # событие смещения мыши
        if event.type == pygame.MOUSEMOTION:
            x2, y2 = event.pos
    # рисуем сохраненные прямоугольники
    for i in range(len(start_x)):
        pygame.draw.rect(screen, rect_color,
                         ((start_x[i], start_y[i]), (rect_width[i], rect_height[i])), 5)
    # если в данный момент левая клавиша зажата, значит рисуем еще один прямоугольник
    if drawing:
        pygame.draw.rect(screen, rect_color, ((x1, y1), (x2 - x1, y2 - y1)), 5)

    pygame.display.flip()
pygame.quit()
