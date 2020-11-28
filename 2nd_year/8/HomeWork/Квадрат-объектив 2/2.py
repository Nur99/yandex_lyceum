import sys

from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit

SCREEN_SIZE = [500, 500]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.draw.clicked.connect(self.drawf)

    def initUI(self):
        self.setGeometry(500, 500, *SCREEN_SIZE)
        self.setWindowTitle('Квадрат - объектив')

        # Ввод коэффициента
        self.lbl1 = QLabel(self)
        self.lbl1.setText("K = ")
        self.lbl1.move(10, 20)

        self.k = QLineEdit(self)
        self.k.move(40, 20)

        # Ввод числа повторов
        self.lbl2 = QLabel(self)
        self.lbl2.setText("N = ")
        self.lbl2.move(180, 20)

        self.n = QLineEdit(self)
        self.n.move(210, 20)

        self.draw = QPushButton("Рисовать", self)
        self.draw.move(350, 15)

    def xs(self, x):
        return x + SCREEN_SIZE[0] // 2

    def ys(self, y):
        return SCREEN_SIZE[1] // 2 - y

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.drawSq()
            self.qp.end()

    def scale(self, p1, p2, k):
        return p1[0] + k * (p2[0] - p1[0]), p1[1] + k * (p2[1] - p1[1])

    def create_polygon(self, nodes):
        nodes2 = [(self.xs(node[0]), self.ys(node[1])) for node in nodes]
        for i in range(-1, len(nodes2) - 1):
            self.qp.drawLine(*nodes2[i], *nodes2[i + 1])

    def drawSq(self):
        if self.k.text() != '' and self.n.text() != '':
            k = float(self.k.text())
            n = int(self.n.text())
            nodes = [(100, 100), (-100, 100), (-100, -100), (100, -100)]
            for i in range(n):
                self.create_polygon(nodes)
                new_nodes = []
                for index in range(-1, len(nodes) - 1):
                    new_nodes.append(self.scale(nodes[index], nodes[index + 1], k))
                nodes = new_nodes[:]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
