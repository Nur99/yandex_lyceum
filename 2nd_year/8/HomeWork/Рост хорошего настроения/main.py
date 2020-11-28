import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class GoodMoodRising(QMainWindow):
    def __init__(self):
        super(GoodMoodRising, self).__init__()
        uic.loadUi('main.ui', self)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_smile(qp)
        qp.end()
        self.canvas.update()

    def draw_smile(self, qp: QPainter):
        qp.setPen(QColor(255, 0, 0))
        k = self.slider.value()
        qp.drawEllipse(0, 0, 10 * k, 10 * k)
        qp.drawArc(2 * k, 6 * k, 6 * k, 2 * k, -30 * 16, -120 * 16)
        qp.drawEllipse(0, 0, 10 * k, 10 * k)
        qp.drawEllipse(2 * k, 2 * k, 2 * k, 2 * k)
        qp.drawEllipse(6 * k, 2 * k, 2 * k, 2 * k)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GoodMoodRising()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
