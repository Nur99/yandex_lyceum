import sys

from PyQt5.QtWidgets import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 300, 320, 500)
        self.setWindowTitle('Азбука Морзе 2')

        self.radio1 = QRadioButton("X", self)
        self.radio1.move(120, 30)
        self.radio1.setChecked(True)
        self.radio2 = QRadioButton("0", self)
        self.radio2.move(160, 30)
        self.first_time = True
        self.blocks = []
        self.start = 'X'
        self.game_stopped = False
        self.lable = QLabel("\t\t\t\t", self)
        self.lable.move(100, 300)
        font = self.lable.font()
        font.setPointSize(16)
        font.setBold(True)
        self.lable.setFont(font)

        self.ng = QPushButton("Новая игра", self)
        self.ng.move(110, 350)
        self.ng.clicked.connect(self.new_game)

        for i in range(3):
            for j in range(3):
                self.blocks.append(QPushButton(self))
                self.blocks[i * 3 + j].move(i * 70 + 50, j * 70 + 60)
                self.blocks[i * 3 + j].resize(70, 70)
                self.blocks[i * 3 + j].clicked.connect(self.click_box)


    def click_box(self):
        if not self.game_stopped:
            self.sender().setText(self.start)
            if self.start == 'X':
                self.start = '0'
            else:
                self.start = 'X'
            self.check_win()

    def check_win(self):
        winner = ""
        mat = []
        for i in range(3):
            mat.append([])
            for j in range(3):
                 mat[i].append(self.blocks[i * 3 + j].text())

        print(mat)
        for i in range(3):
            if "".join(mat[i]) == 'XXX':
               winner = "X"
            if "".join(mat[i]) == '000':
               winner = "0"

        nmat = []
        for i in range(3):
            nmat.append([])
            for j in range(3):
                nmat[i].append(mat[j][i])

        mat = nmat
        for i in range(3):
            if "".join(mat[i]) == 'XXX':
               winner = "X"
            if "".join(mat[i]) == '000':
               winner = "0"

        if mat[0][0] == mat[1][1] == mat[2][2]:
            if mat[0][0] == 'X':
                winner = 'X'
            if mat[0][0] == '0':
                winner = '0'

        if mat[0][2] == mat[1][1] == mat[2][0]:
            if mat[0][2] == 'X':
                winner = 'X'
            if mat[0][2] == '0':
                winner = '0'

        if winner == 'X' or winner == '0':
            self.lable.setText(f"Won {winner}")
            self.stop_game()

        if len("".join(mat[0]) + "".join(mat[1]) + "".join(mat[2])) == 9:
            self.lable.setText(f"  Draw")
            self.stop_game()

    def new_game(self):
        self.game_stopped = False
        for i in range(9):
            self.blocks[i].setText("")
        if self.radio2.isChecked():
            self.start = '0'
        else:
            self.start = 'X'

    def stop_game(self):
        self.game_stopped = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
