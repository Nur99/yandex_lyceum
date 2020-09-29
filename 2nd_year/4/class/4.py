import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QLCDNumber
import PyQt5.QtGui as QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Миникалькулятор')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 80)
        self.button_1.resize(100, 25)
        self.button_1.setText('->')
        self.button_1.clicked.connect(self.run)

        self.label1 = QLabel('Первое число (целое):', self)
        self.label1.move(20, 15)

        self.label2 = QLabel('Второе число (целое):', self)
        self.label2.move(20, 145)

        self.lab_1 = QLineEdit(self)
        self.lab_1.move(20, 30)
        self.lab_1.resize(100, 15)

        self.lab_2 = QLineEdit(self)
        self.lab_2.move(20, 160)
        self.lab_2.resize(100, 15)

        self.summ = QLCDNumber(self)
        self.summ.move(230, 30)
        self.summl = QLabel('Сумма:', self)
        self.summl.move(190, 35)

        self.razn = QLCDNumber(self)
        self.razn.move(230, 60)
        self.raznl = QLabel('Разность:', self)
        self.raznl.move(180, 65)

        self.proiz = QLCDNumber(self)
        self.proiz.move(230, 90)
        self.proizl = QLabel('Произведение:', self)
        self.proizl.move(153, 95)

        self.chas = QLCDNumber(self)
        self.chas.move(230, 120)
        self.chasl = QLabel('Частное:', self)
        self.chasl.move(180, 125)

    def run(self):
        f = int(self.lab_1.text())
        s = int(self.lab_2.text())
        self.summ.display(f + s)
        self.razn.display(f - s)
        self.proiz.display(f * s)
        if s != 0:
            self.chas.display(f / s)
        else:
            self.chas.display('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
