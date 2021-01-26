import pygame
import requests
import sys
import os

map_requests = [
    "http://static-maps.yandex.ru/1.x/?ll=2.294458,48.858302&spn=0.001,0.001&l=sat",
    # Эйфелева башня:
    "http://static-maps.yandex.ru/1.x/?ll=158.859569,53.242235&spn=0.05,0.05&l=sat",
    # Авачинский вулкан:
    "http://static-maps.yandex.ru/1.x/?ll=63.341294,45.921277&spn=0.005,0.005&l=sat"
    # Площадка Байконура "Гагаринсий старт"
]


class MyError(Exception):
    pass


def load_next_slide(counter):
    # Запрашиваем изображение.
    request = map_requests[counter % len(map_requests)]
    response = requests.get(request)
    if not response:
        print("Ошибка выполнения запроса:", file=sys.stderr)
        print(request, file=sys.stderr)
        print("Http статус:", response.status_code, "(", response.reason, ")", file=sys.stderr)
        raise MyError()

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        raise MyError()

    surface = pygame.image.load(map_file)

    os.remove(map_file)
    return surface


def draw_next_slide(screen, counter):
    # Загружаем слайд.
    slide = load_next_slide(counter)
    # Рисуем слайд.
    screen.blit(slide, (0, 0))
    # Переключаем экран.
    pygame.display.flip()
    return counter + 1


def run_slide_show(screen):
    slide_counter = draw_next_slide(screen, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYUP:
                slide_counter = draw_next_slide(screen, slide_counter)


def main():
    # Инициализируем pygame
    pygame.init()
    try:
        run_slide_show(pygame.display.set_mode((600, 450)))
    except MyError as ex:
        pass
    pygame.quit()


if __name__ == "__main__":
    main()
