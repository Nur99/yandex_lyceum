import sys
import random

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.setBrushColor()
            self.draw(self.status)
            self.qp.end()

    def setBrushColor(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.qp.setBrush(QColor(self.r, self.g, self.b))

    def draw(self, status):
        self.size = random.randint(10, 100)
        if status == 1:
            self.qp.drawEllipse(*self.coords_, self.size, self.size)
        elif status == 2:
            self.qp.drawRect(*self.coords_, self.size, self.size)
        elif status == 3:
            x, y = self.coords_
            self.qp.drawPolygon(QPolygon([
                QPoint(x, y - self.size),
                QPoint(x + self.size, y + self.size),
                QPoint(x - self.size, y + self.size)
            ]))

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')

        self.show()

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.status = 1
        elif event.button() == Qt.RightButton:
            self.status = 2
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.status = 3
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
