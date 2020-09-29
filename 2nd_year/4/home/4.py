import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QPlainTextEdit, QCheckBox


class Focus(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 400, 285, 310)
        self.setWindowTitle('Заказ в Макдональдсе')

        menu = ['Чизбургер', 'Кока-кола', 'Гамбургер', 'Нагетсы']
        r = []
        x = 10
        y = 10
        self.kt = []
        for i in range(4):
            r.append(i)
            r[i] = QCheckBox(menu[i], self)
            r[i].move(x, y)
            y += 17
            r[i].stateChanged.connect(self.conv)

        y += 10
        self.btn = QPushButton('Заказать', self)
        self.btn.move(x, y)
        self.btn.resize(90, 45)
        y += 60
        self.btn.clicked.connect(self.conv2)

        self.txt = QPlainTextEdit(self)
        self.txt.setGeometry(x, y, 100, 150)
        self.txt.setReadOnly(True)

    def conv(self, state):
        if state:
            self.kt.append(self.sender().text())
        else:
            self.kt.remove(self.sender().text())

    def conv2(self):
        self.txt.clear()
        if len(self.kt) > 0:
            self.txt.appendPlainText('Ваш заказ:')
            self.txt.appendPlainText('')
            for i in range(len(self.kt)):
                self.txt.appendPlainText(self.kt[i])
        else:
            self.txt.appendPlainText('Вы ничего не заказали :(')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())

