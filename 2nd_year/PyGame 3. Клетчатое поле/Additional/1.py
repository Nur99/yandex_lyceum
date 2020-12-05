import pygame
from random import randint

FIRST_PLAYER = 1
SECOND_PLAYER = 2


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[FIRST_PLAYER if randint(0, 1) else SECOND_PLAYER for _ in range(width)] for _
                      in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.red = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.width):
            for e in range(self.height):
                clr = pygame.Color("black")
                if self.board[e][i] == FIRST_PLAYER:
                    clr = pygame.Color("red")
                else:
                    clr = pygame.Color("blue")
                pygame.draw.circle(screen, clr,
                                   (self.left + i * self.cell_size + self.cell_size // 2,
                                    self.top + e * self.cell_size + self.cell_size // 2),
                                   self.cell_size // 2 - 2, 0)
                pygame.draw.rect(screen, pygame.Color("white"),
                                 pygame.Rect(self.left + i * self.cell_size,
                                             self.top + e * self.cell_size,
                                             self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if self.cell_size * self.width > mouse_pos[0] - self.left > 0:
            if mouse_pos[1] - self.left > 0 and mouse_pos[1] - \
                    self.top < self.cell_size * self.height:
                return (mouse_pos[0] - self.left) // self.cell_size, (
                        mouse_pos[1] - self.top) // self.cell_size

    def on_click(self, cell):
        if cell:
            if self.red and self.board[cell[1]][cell[0]] == FIRST_PLAYER:
                for i in range(self.height):
                    self.board[i][cell[0]] = FIRST_PLAYER
                for i in range(self.width):
                    self.board[cell[1]][i] = FIRST_PLAYER
                self.red = not self.red
            elif not self.red and self.board[cell[1]][cell[0]] == SECOND_PLAYER:
                for i in range(self.height):
                    self.board[i][cell[0]] = SECOND_PLAYER
                for i in range(self.width):
                    self.board[cell[1]][i] = SECOND_PLAYER
                self.red = not self.red

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def main():
    pygame.init()
    pygame.display.set_caption('Недореверси')

    size = 600, 600
    screen = pygame.display.set_mode(size)
    running = True
    board = Board(8, 8)
    board.set_view(100, 100, 50)
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
