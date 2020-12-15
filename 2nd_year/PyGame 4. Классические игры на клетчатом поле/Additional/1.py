import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 20

        # настройка внешнего вида

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    into = 1
                else:
                    into = 0
                col = self.col[self.board[i][j]]
                pygame.draw.rect(screen, pygame.Color("white"), (
                    self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size,
                    self.cell_size),
                                 into)
                pygame.draw.rect(screen, pygame.Color(col), (
                    self.left + j * self.cell_size + 1, self.top + i * self.cell_size + 1,
                    self.cell_size - 2,
                    self.cell_size - 2),
                                 into)


class LifeBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        # константы
        self.col = ("black", "green")

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] < self.left or mouse_pos[0] > self.left + self.cell_size * len(
                self.board[0]) or mouse_pos[1] \
                < self.top or mouse_pos[1] > self.top + self.cell_size * len(self.board):
            return None
        return (
            (mouse_pos[0] - self.left) // self.cell_size,
            (mouse_pos[1] - self.top) // self.cell_size)

    def on_click(self, cell):
        if cell == None:
            return
        self.board[cell[1]][cell[0]] = ((self.board[cell[1]][cell[0]]) + 1) % len(self.col)

    def get_neighbours(self, i, j):
        cnt = 0
        for ii in range(i - 1, i + 2):
            for jj in range(j - 1, j + 2):
                if ii < 0:
                    ii = len(self.board) - 1
                elif ii >= len(self.board):
                    ii = 0
                if jj < 0:
                    jj = len(self.board[ii]) - 1
                elif jj >= len(self.board[ii]):
                    jj = 0
                if i == ii and j == jj:
                    continue
                elif self.board[ii][jj] == 1:
                    cnt += 1
        return cnt

    def step(self):
        self.new_board = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                cnt = self.get_neighbours(i, j)
                if cnt not in (2, 3) and self.board[i][j] == 1:
                    self.new_board[i][j] = 0
                elif cnt == 3 and self.board[i][j] == 0:
                    self.new_board[i][j] = 1
                else:
                    self.new_board[i][j] = self.board[i][j]
        self.board = deepcopy(self.new_board)


def main():
    fps = 10
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    screen.fill((0, 0, 0))
    pygame.display.set_caption('Жизнь на Торе')
    # board = LifeBoard(59, 44)
    board = LifeBoard(18, 18)
    running = True
    play_flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.get_click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                play_flag = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                fps += 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                fps -= 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                play_flag = not play_flag
        if fps < 1:
            fps = 1
        if play_flag:
            board.step()
        screen.fill((0, 0, 0))
        board.render(screen)
        if play_flag:
            clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
