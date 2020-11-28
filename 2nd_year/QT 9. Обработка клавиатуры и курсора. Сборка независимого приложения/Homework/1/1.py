import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
import random


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.coords = [20, 40]
        self.delta = 10
        self.btn_size = [120, 40]
        self.setMouseTracking(True)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Убегающая кнопка')
        self.button_1 = QPushButton(self)
        self.button_1.move(*self.coords)
        self.button_1.resize(*self.btn_size)
        self.button_1.setText("Нажми меня")
        self.show()

    def mouseMoveEvent(self, event):
        ## Если указатель мыши попадает в диапазон вокруг кнопки, то кнопка перемещается в случайное место на экране
        if (event.x() in range(self.coords[0] - self.delta, self.coords[0] + self.delta + 120)) and (
                event.y() in range(self.coords[1] - self.delta, self.coords[1] + self.delta + 40)):
            self.coords[0] = random.randrange(0, 400 - self.btn_size[0])
            self.coords[1] = random.randrange(0, 400 - self.btn_size[1])
            self.button_1.move(*self.coords)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
