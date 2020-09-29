import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLineEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setFixedSize(400, 150)
        self.setWindowTitle('Арифмометр')

        self.btn1 = QPushButton(self)
        self.btn1.setText('+')
        self.btn1.resize(25, 25)
        self.btn1.move(120, 10)
        self.btn1.clicked.connect(self.name1)

        self.btn2 = QPushButton(self)
        self.btn2.setText('-')
        self.btn2.resize(25, 25)
        self.btn2.move(150, 10)
        self.btn2.clicked.connect(self.name2)

        self.btn3 = QPushButton(self)
        self.btn3.setText('*')
        self.btn3.resize(25, 25)
        self.btn3.move(180, 10)
        self.btn3.clicked.connect(self.name3)

        self.input = QLineEdit(self)
        self.input.move(80, 10)
        self.input.resize(30, 30)

        self.output = QLineEdit(self)
        self.output.move(210, 10)
        self.output.resize(30, 30)

        self.l1 = QLabel(self)
        self.l1.setText("=")
        self.l1.move(240, 20)

        self.res = QLineEdit(self)
        self.res.move(250, 10)
        self.res.resize(30, 30)

    def name1(self):
        self.res.setText(str(int(self.input.text()) + int(self.output.text())))

    def name2(self):
        self.res.setText(str(int(self.input.text()) - int(self.output.text())))

    def name3(self):
        self.res.setText(str(int(self.input.text()) * int(self.output.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
