import sys
from math import pi, cos, sin

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QColorDialog

SCREEN_SIZE = [500, 500]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.draw.clicked.connect(self.drawf)

    def initUI(self):
        self.setGeometry(500, 500, *SCREEN_SIZE)
        self.setWindowTitle('Не квадрат - объектив')

        # Ввод коэффициента
        self.lbl1 = QLabel(self)
        self.lbl1.setText("K = ")
        self.lbl1.move(10, 20)

        self.k = QLineEdit(self)
        self.k.move(40, 20)
        self.k.resize(50, 20)

        # Ввод числа повторов
        self.lbl2 = QLabel(self)
        self.lbl2.setText("N = ")
        self.lbl2.move(130, 20)

        self.n = QLineEdit(self)
        self.n.move(160, 20)
        self.n.resize(50, 20)

        # Ввод размера фигуры
        self.lbl3 = QLabel(self)
        self.lbl3.setText("M = ")
        self.lbl3.move(250, 20)

        self.m = QLineEdit(self)
        self.m.move(280, 20)
        self.m.resize(50, 20)

        self.draw = QPushButton("Рисовать", self)
        self.draw.move(350, 15)

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def drawf(self):
        self.color = QColorDialog.getColor()
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setPen(self.color)
            self.drawSq()
            self.qp.end()

    def scale(self, p1, p2, k):
        return p1[0] + k * (p2[0] - p1[0]), p1[1] + k * (p2[1] - p1[1])

    def create_polygon(self, nodes):
        nodes2 = [(self.xs(node[0]), self.ys(node[1])) for node in nodes]
        for i in range(-1, len(nodes2) - 1):
            self.qp.drawLine(*nodes2[i], *nodes2[i + 1])

    def drawSq(self):

        if self.k.text() != '' and self.n.text() != '' and self.m.text() != '':
            k = float(self.k.text())
            n = int(self.n.text())
            p = int(self.m.text())
            RAD = 100
            nodes = [(RAD * cos(i * 2 * pi / p), RAD * sin(i * 2 * pi / p)) for i in range(p)]
            for i in range(n):
                self.create_polygon(nodes)
                new_nodes = []
                for index in range(-1, len(nodes) - 1):
                    new_nodes.append(self.scale(nodes[index], nodes[index + 1], k))
                nodes = new_nodes[:]

def except_hook(cls, exception, traceback):
    sys.__except_hook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
