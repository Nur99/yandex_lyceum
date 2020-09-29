import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(450, 150, 450, 150)
        self.setWindowTitle('Миникалькулятор')
        self.btn = QPushButton('->', self)
        self.label1 = QLineEdit(self)
        self.label2 = QLineEdit(self)
        self.labe1 = QLabel(self)
        self.labe2 = QLabel(self)
        self.labe3 = QLabel(self)
        self.labe4 = QLabel(self)
        self.q1 = QLCDNumber(self)
        self.q2 = QLCDNumber(self)
        self.q3 = QLCDNumber(self)
        self.q4 = QLCDNumber(self)
        self.label1.move(5, 25)
        self.label2.move(5, 65)
        self.btn.resize(20, 20)
        self.btn.move(150, 55)
        self.labe1.setText("Сумма")
        self.labe2.setText("Разность")
        self.labe3.setText("Произведение")
        self.labe4.setText("Частность")
        self.labe1.move(175, 5)
        self.labe2.move(175, 35)
        self.labe3.move(175, 65)
        self.labe4.move(175, 95)
        self.q1.move(270, 5)
        self.q2.move(270, 35)
        self.q3.move(270, 65)
        self.q4.move(270, 95)
        self.btn.clicked.connect(self.nn)
    
    def nn(self):
        e = int(self.label1.text())
        w = int(self.label2.text())
        self.q1.display(e + w)
        self.q2.display(e - w)
        self.q3.display(e * w)
        if w != 0: self.q4.display(e / w)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec()) 