import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QLCDNumber
a = {'a': '.-'}
a['b'] = '-...'
a['c'] = '-.-.'
a['d'] = '-..'
a['e'] = '.'
a['f'] = '..-.'
a['g'] = '--.'
a['h'] = '....'
a['i'] = '..'
a['j'] = '.---'
a['k'] = '-.-'
a['l'] = '.-..'
a['m'] = '--'
a['n'] = '-.'
a['o'] = '---'
a['p'] = '.--.'
a['q'] = '--.-'
a['r'] = '.-.'
a['s'] = '...'
a['t'] = '-'
a['u'] = '..-'
a['v'] = '...-'
a['w'] = '.--'
a['x'] = '-..-'
a['y'] = '-.--'
a['z'] = '--..'


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 150, 400, 150)
        self.setWindowTitle('Азбука Морзе 2')
        b = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(b)):
            self.qw = QPushButton(b[i], self)
            self.qw.resize(20, 20)
            self.qw.move(20 * (i % 13), 20 * (i // 13 + 1))
            self.qw.clicked.connect(self.x)
        self.label = QLineEdit(self)
        self.label.resize(260, 20)
        self.label.move(5, 60)
        self.show()

    def x(self):
        global a
        self.label.setText(self.label.text() + a[self.sender().text()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec()) 
