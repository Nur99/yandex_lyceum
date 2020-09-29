import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5.QtWidgets import QLabel, QLCDNumber


class Focus(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(600, 400, 520, 170)
        self.setWindowTitle('Миникалькулятор')

        self.l1 = QLabel(self)
        self.l1.move(10, 15)
        self.l1.setText('Первое число(целое):')

        self.l2 = QLabel(self)
        self.l2.move(10, 85)
        self.l2.setText('Второе число(целое):')

        self.st1 = QLineEdit(self)
        self.st1.move(10, 40)
        self.st1.resize(130, 30)

        self.st2 = QLineEdit(self)
        self.st2.move(10, 110)
        self.st2.resize(130, 30)

        self.btn = QPushButton(self)
        self.btn.setText('->')
        self.btn.setGeometry(150, 75, 130, 30)
        self.btn.clicked.connect(self.conv)

        self.c1 = QLCDNumber(self)
        self.c1.move(370, 10)
        self.c1.resize(130, 30)

        self.c2 = QLCDNumber(self)
        self.c2.move(370, 50)
        self.c2.resize(130, 30)

        self.c3 = QLCDNumber(self)
        self.c3.move(370, 90)
        self.c3.resize(130, 30)

        self.c4 = QLCDNumber(self)
        self.c4.move(370, 130)
        self.c4.resize(130, 30)

        self.l3 = QLabel(self)
        self.l3.move(330, 20)
        self.l3.setText('Сумма:')

        self.l4 = QLabel(self)
        self.l4.move(315, 60)
        self.l4.setText('Разность:')

        self.l5 = QLabel(self)
        self.l5.move(290, 100)
        self.l5.setText('Произведение:')

        self.l6 = QLabel(self)
        self.l6.move(320, 140)
        self.l6.setText('Частное:')

        self.n = 0

    def conv(self):
        self.c1.display(int(int(self.st1.text()) + int(self.st2.text())))
        self.c2.display(int(int(self.st1.text()) - int(self.st2.text())))
        self.c3.display(int(int(self.st1.text()) * int(self.st2.text())))
        if int(self.st2.text()) != 0:
            self.c4.display(int(self.st1.text()) / int(self.st2.text()))
        else:
            self.c4.display("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())
