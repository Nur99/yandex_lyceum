import copy
import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # cell - кортеж (x, y)
    def on_click(self, cell):
        # заглушка для реальных игровых полей
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell and cell < (self.width, self.height):
            self.on_click(cell)


class Lines(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.selected_cell = None
        self.distances = dict()

    def has_path(self, x1, y1, x2, y2):
        # словарь расстояний
        d = {(x1, y1): 0}
        v = [(x1, y1)]
        while len(v) > 0:
            x, y = v.pop(0)
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx * dy != 0:
                        continue
                    if x + dx < 0 or x + dx >= self.width or y + dy < 0 or y + dy >= self.height:
                        continue
                    if self.board[y + dy][x + dx] == 0:
                        dn = d.get((x + dx, y + dy), -1)
                        if dn == -1:
                            d[(x + dx, y + dy)] = d.get((x, y), -1) + 1
                            v.append((x + dx, y + dy))
        dist = d.get((x2, y2), -1)
        return dist >= 0, d

    def on_click(self, cell):

        x = cell[0]
        y = cell[1]
        if self.selected_cell is None:

            if self.board[y][x] == 1:
                self.selected_cell = x, y
            else:
                self.board[y][x] = 1

        else:
            if self.selected_cell == (x, y):
                self.selected_cell = None
                return

            x2 = self.selected_cell[0]
            y2 = self.selected_cell[1]
            has_path, distances = self.has_path(x2, y2, x, y)
            if has_path:
                self.board[y][x] = 1
                self.board[y2][x2] = 0
                self.distances = distances
                self.selected_cell = None

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                font = pygame.font.Font(None, self.cell_size - 6)
                text = font.render(str(self.distances.get((x,y), -1)), 1, (100, 255, 100))
                screen.blit(text, (
                    x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 3))
                if self.board[y][x] == 1:
                    color = pygame.Color("blue")
                    if self.selected_cell == (x, y):
                        color = pygame.Color("red")
                    pygame.draw.ellipse(screen, color,
                                        (x * self.cell_size + self.left,
                                         y * self.cell_size + self.top, self.cell_size,
                                         self.cell_size))

                pygame.draw.rect(screen, pygame.Color(255, 255, 255),
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)


def main():
    pygame.init()
    size = 420, 420
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Линеечки')

    board = Lines(10, 10)
    board.set_view(10, 10, 40)

    ticks = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        if ticks == 50:
            ticks = 0
        pygame.display.flip()
        clock.tick(50)
        ticks += 1
    pygame.quit()


if __name__ == '__main__':
    main()
