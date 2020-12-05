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

        # чей ход
        self.crosses = True

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size - 3 + self.cell_size), 2)
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (self.left + x * self.cell_size + 3,
                                      self.top + y * self.cell_size + self.cell_size - 3),
                                     (self.left + x * self.cell_size - 3 + self.cell_size,
                                      self.top + y * self.cell_size + 3), 2)
                if self.board[y][x] == 2:
                    pygame.draw.ellipse(screen, pygame.Color("red"), (
                        (self.left + x * self.cell_size + 3, self.top + y * self.cell_size + 3),
                        (self.cell_size - 6, self.cell_size - 6)), 2)
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # cell - кортеж (x, y)
    def on_click(self, cell):
        if self.board[cell[1]][cell[0]] == 0:
            if self.crosses:
                self.board[cell[1]][cell[0]] = 1
            else:
                self.board[cell[1]][cell[0]] = 2
            self.crosses = not self.crosses

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


def main():
    pygame.init()
    size = 320, 230
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Пра-пра-пра-крестики-нолики')

    # поле 5 на 7
    board = Board(10, 7)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
