import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLCDNumber


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.t = ""
        self.calcul = ""
        self.expr = ""
        uic.loadUi('calc.ui', self)
        self.btn1.clicked.connect(self.add_number)
        self.btn2.clicked.connect(self.add_number)
        self.btn3.clicked.connect(self.add_number)
        self.btn4.clicked.connect(self.add_number)
        self.btn5.clicked.connect(self.add_number)
        self.btn6.clicked.connect(self.add_number)
        self.btn7.clicked.connect(self.add_number)
        self.btn8.clicked.connect(self.add_number)
        self.btn9.clicked.connect(self.add_number)
        self.btn0.clicked.connect(self.add_number)
        self.btn_pow.clicked.connect(self.add_expression)
        self.btn_dot.clicked.connect(self.add_number)
        self.btn_plus.clicked.connect(self.add_expression)
        self.btn_minus.clicked.connect(self.add_expression)
        self.btn_mult.clicked.connect(self.add_expression)
        self.btn_div.clicked.connect(self.add_expression)
        self.btn_eq.clicked.connect(self.calulate)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_sqrt.clicked.connect(self.add_expression)
        self.btn_fact.clicked.connect(self.add_expression)

    def add_number(self):
        self.t += self.sender().text()
        try:
            if self.t[-1] == self.t[-2] == ".":
                self.t.pop()
        except:
            pass
        if self.t != "":
            self.table.display(self.t)

    def add_expression(self):
        self.calcul += self.t
        self.expr = self.sender().text()
        self.calcul += self.expr
        self.t = ""

    def clear(self):
        self.t = ""
        self.calcul = ""
        self.table.display("")

    def calulate(self):
        self.calcul += self.t
        self.t = ""

        if "^" in self.calcul:
            self.calcul = self.calcul.replace("^", "**")

        if '√' in self.calcul:
            self.calcul = self.calcul.replace('√', "**0.5")

        self.f = 1
        if '!' in self.calcul:
            self.cal = self.calcul.pop()
            for i in range(1, int(self.cal) + 1):
                self.f *= i
            self.calcul = ''
            self.calcul += self.f
            self.calcul += '+0'

        self.calcul = str(eval(self.calcul))
        self.table.display(self.calcul)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
