import pygame
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("map", type=str, nargs="?", default="map.map")
args = parser.parse_args()
map_file = args.map


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
FPS = 50

tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50


class SpriteGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def shift(self, vector):
        global level_map
        if vector == "up":
            max_lay_y = max(self, key=lambda sprite: sprite.abs_pos[1]).abs_pos[1]
            print('MAX lay y', max_lay_y)
            for sprite in self:
                sprite.abs_pos[1] -= (tile_height * max_y
                                      if sprite.abs_pos[1] == max_lay_y else 0)
        elif vector == "down":
            min_lay_y = min(self, key=lambda sprite: sprite.abs_pos[1]).abs_pos[1]
            print(min_lay_y)
            for sprite in self:
                sprite.abs_pos[1] += (tile_height * max_y
                                      if sprite.abs_pos[1] == min_lay_y else 0)
        elif vector == "left":
            max_lay_x = max(self, key=lambda sprite: sprite.abs_pos[0]).abs_pos[0]
            print(max_lay_x)
            for sprite in self:
                if sprite.abs_pos[0] == max_lay_x:
                    sprite.abs_pos[0] -= tile_width * max_x
        elif vector == "right":
            min_lay_x = min(self, key=lambda sprite: sprite.abs_pos[0]).abs_pos[0]
            print(min_lay_x)
            for sprite in self:
                sprite.abs_pos[0] += (tile_height * max_x
                                      if sprite.abs_pos[0] == min_lay_x else 0)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(sprite_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.abs_pos = [self.rect.x, self.rect.y]

    def set_pos(self, x, y):
        self.abs_pos = [x, y]


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(hero_group)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        camera.dx -= tile_width * (x - self.pos[0])
        camera.dy -= tile_height * (y - self.pos[1])
        # print(camera.dx, camera.dy)
        self.pos = (x, y)
        for sprite in sprite_group:
            camera.apply(sprite)


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x = obj.abs_pos[0] + self.dx
        obj.rect.y = obj.abs_pos[1] + self.dy

    def update(self, target):
        self.dx = 0
        self.dy = 0


running = True
clock = pygame.time.Clock()
sprite_group = SpriteGroup()
hero_group = SpriteGroup()


def terminate():
    pygame.quit()
    sys.exit


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "",
                  "На торе"]

    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = "."
    return new_player, x, y


def move(hero, movement):
    x, y = hero.pos
    if movement == "up":
        prev_y = y - 1 if y != 0 else max_y
        print(prev_y)
        if level_map[prev_y][x] == ".":
            if prev_y == max_y:
                for i in range(max_y - 1):
                    sprite_group.shift("down")
                hero.move(x, prev_y - 1)
            else:
                sprite_group.shift("up")
                hero.move(x, prev_y)
    elif movement == "down":
        next_y = y + 1 if y != max_y else 0
        if level_map[next_y][x] == ".":
            if next_y == 0:
                for i in range(max_y - 1):
                    sprite_group.shift("up")
                hero.move(x, next_y + 1)
            else:
                sprite_group.shift("down")
                hero.move(x, next_y)
    elif movement == "left":
        prev_x = x - 1 if x != 0 else max_x
        if level_map[y][prev_x] == ".":
            if prev_x == max_x:
                for i in range(max_x - 1):
                    sprite_group.shift("right")
                hero.move(prev_x - 1, y)
            else:
                sprite_group.shift("left")
                hero.move(prev_x, y)
    elif movement == "right":
        next_x = x + 1 if x != max_x else 0
        if level_map[y][next_x] == ".":
            if next_x == 0:
                for i in range(max_x - 1):
                    sprite_group.shift("left")
                hero.move(next_x + 1, y)
            else:
                sprite_group.shift("right")
                hero.move(next_x, y)


start_screen()
camera = Camera()
level_map = load_level(map_file)
hero, max_x, max_y = generate_level(level_map)
print(max_x, max_y)
camera.update(hero)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move(hero, "up")
            elif event.key == pygame.K_DOWN:
                move(hero, "down")
            elif event.key == pygame.K_LEFT:
                move(hero, "left")
            elif event.key == pygame.K_RIGHT:
                move(hero, "right")
    screen.fill(pygame.Color("black"))
    sprite_group.draw(screen)
    hero_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
