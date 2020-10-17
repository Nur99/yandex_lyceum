import sys

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyPillow(QMainWindow):
    def __init__(self):
        super(MyPillow, self).__init__()
        uic.loadUi('main.ui', self)
        self.app = app

        self.filename = QFileDialog.getOpenFileName(self, 'Выберите картинку', '', 'Картинки (*.jpg)')[0]
        self.orig_image = Image.open(self.filename)
        self.curr_image = Image.open(self.filename)
        self.degree = 0
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)
        for button in self.channelButtons.buttons():
            button.clicked.connect(self.set_channel)
        for button in self.rotateButtons.buttons():
            button.clicked.connect(self.rotate)

    def set_channel(self):
        self.curr_image = self.orig_image.copy()
        pixels = self.curr_image.load()
        x, y = self.curr_image.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if (self.sender().text() == 'R'):
                    pixels[i, j] = r, 0, 0
                elif (self.sender().text() == 'G'):
                    pixels[i, j] = 0, g, 0
                elif (self.sender().text() == 'B'):
                    pixels[i, j] = 0, 0, b
                else:
                    pass
        self.curr_image = self.curr_image.rotate(self.degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.pushButton_6:
            self.degree -= 90
            degree = -90
        else:
            self.degree += 90
            degree = 90
        self.degree %= 360
        self.curr_image = self.curr_image.rotate(degree, expand=True)
        # python 3.8 garbage collection issue
        self.a = ImageQt(self.curr_image)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()

    sys.exit(app.exec())
