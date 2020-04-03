import copy


class TicTacToeBoard:

    def __init__(self):
        self.new_game()

    def new_game(self):
        self.board = [["-", "-", "-"] for _ in range(3)]
        self.move = 'X'
        self.in_process = True
        self.winner = None

    def get_field(self):
        return copy.deepcopy(self.board)

    def check_field(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '-':
                self.winner = self.board[i][0]
                break
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '-':
                self.winner = self.board[0][i]
                break
        if not self.winner and (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                                self.board[0][2] == self.board[1][1] == self.board[2][0]) and \
                self.board[1][1] != '-':
            self.winner = self.board[1][1]
        if "-" not in "".join(self.board[0]) + "".join(self.board[0]) + "".join(self.board[0]) and not self.winner:
            self.winner = "D"
        if self.winner:
            self.in_process = False
            return self.winner
        else:
            return None

    def make_move(self, row, col):
        if not self.in_process:
            return "Игра уже завершена"
        if self.board[row - 1][col - 1] != "-":
            return f"Клетка {row}, {col} уже занята"
        self.board[row - 1][col - 1] = self.move
        if self.move == 'X':
            self.move = '0'
        else:
            self.move = 'X'
        winner = self.check_field()
        if winner == "X":
            return "Победил игрок X"
        elif winner == "0":
            return "Победил игрок 0"
        elif winner == "D":
            return "Ничья"
        else:
            return "Продолжаем играть"
