import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.current = 'ufo.gif'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Управление НЛО')

        self.pixmap = QPixmap(self.current)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.delta = 10

        self.show()

    ## Обработка нажатия на клавиатуру
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            ## Проверка за вылет с экрана
            if (self.lbl.x() - self.delta < 0):
                self.lbl.move(250, self.lbl.y())
            else:
                self.lbl.move(self.lbl.x() - self.delta, self.lbl.y())
        elif event.key() == Qt.Key_Right:
            if (self.lbl.x() + self.delta > 250):
                self.lbl.move(0, self.lbl.y())
            else:
                self.lbl.move(self.lbl.x() + self.delta, self.lbl.y())
        elif event.key() == Qt.Key_Up:
            if (self.lbl.y() - self.delta < 0):
                self.lbl.move(self.lbl.x(), 250)
            else:
                self.lbl.move(self.lbl.x(), self.lbl.y() - self.delta)
        elif event.key() == Qt.Key_Down:
            if (self.lbl.y() + self.delta > 250):
                self.lbl.move(self.lbl.x(), 0)
            else:
                self.lbl.move(self.lbl.x(), self.lbl.y() + self.delta)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
