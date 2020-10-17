from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor
import sys

SCREEN_SIZE = [400, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('Квадрат объектив 1')
        self.btn = QPushButton(self)
        self.btn.setText('Показать')
        self.btn.move(10, 10)

        self.label = QLabel(self)
        self.label.move(150, 10)
        self.label.setText('side')
        self.lineEdit = QLineEdit(str(300), self)
        self.lineEdit.move(200, 10)

        self.label_2 = QLabel(self)
        self.label_2.move(150, 40)
        self.label_2.setText('coeff')
        self.lineEdit_2 = QLineEdit(str(0.9), self)
        self.lineEdit_2.move(200, 40)

        self.label_3 = QLabel(self)
        self.label_3.move(150, 70)
        self.label_3.setText('n')
        self.lineEdit_3 = QLineEdit(str(10), self)
        self.lineEdit_3.move(200, 70)

        self.flag = False
        self.btn.clicked.connect(self.draw)

    def draw(self):
        self.side = float(self.lineEdit.text())
        self.coef = float(self.lineEdit_2.text())
        self.n = int(self.lineEdit_3.text())
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 0, 0))
            self.x, self.y = SCREEN_SIZE[0] // 2 - self.side // 2, SCREEN_SIZE[1] - self.side - 20

            for _ in range(self.n):
                self.drawSquare(qp)
                DELTA = (self.side * (1 - self.coef)) / 2
                self.side *= self.coef
                self.x += DELTA
                self.y += DELTA
            qp.end()

    def drawSquare(self, qp):
        self.x, self.y, self.side = int(self.x), int(self.y), int(self.side)
        qp.drawLine(self.x, self.y, self.x + self.side, self.y)
        qp.drawLine(self.x + self.side, self.y, self.x + self.side, self.y + self.side)
        qp.drawLine(self.x + self.side, self.y + self.side, self.x, self.y + self.side)
        qp.drawLine(self.x, self.y + self.side, self.x, self.y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
