import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QLCDNumber, QCheckBox
import PyQt5.QtGui as QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Прятки для виджетов')

        self.label1 = QLabel('edit1', self)
        self.label1.move(30, 10)

        self.label2 = QLabel('edit2', self)
        self.label2.move(30, 40)

        self.label3 = QLabel('edit3', self)
        self.label3.move(30, 70)

        self.lab_1 = QLineEdit('Поле edit1', self)
        self.lab_1.move(60, 10)

        self.lab_2 = QLineEdit('Поле edit2', self)
        self.lab_2.move(60, 40)

        self.lab_3 = QLineEdit('Поле edit3', self)
        self.lab_3.move(60, 70)

        self.box1 = QCheckBox(self)
        self.box1.move(10, 10)
        self.box1.h = 0
        self.box1.connector = self.lab_1
        self.box1.clicked.connect(self.run)

        self.box2 = QCheckBox(self)
        self.box2.move(10, 40)
        self.box2.h = 0
        self.box2.connector = self.lab_2
        self.box2.clicked.connect(self.run)

        self.box3 = QCheckBox(self)
        self.box3.move(10, 70)
        self.box3.h = 0
        self.box3.connector = self.lab_3
        self.box3.clicked.connect(self.run)

    def run(self):
        if self.sender().h == 0:
            self.sender().h = 1
            self.sender().connector.hide()
        else:
            self.sender().h = 0
            self.sender().connector.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
