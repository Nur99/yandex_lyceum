import copy
import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        ## Список доступных картинок
        self.cars = ['car2.png', 'car3.png', 'car4.png']
        self.setMouseTracking(True)
        ## Изначальная картинка
        self.current = 'car2.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Машинка')

        self.pixmap = QPixmap(self.cars[0])

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)

        self.show()

    ## Обработка движения мыши
    def mouseMoveEvent(self, event):
        if (event.x() in range(0, 250) and event.y() in range(0, 250)):
            self.lbl.move(event.x(), event.y())

    ## Обработка нажатия на клавиатуру
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            tmp = copy.copy(self.cars)
            tmp.remove(self.current)
            ## Получение случайного изображения
            self.current = random.choice(tmp)
            self.pixmap.load(self.current)
            self.lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
