import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Перемешивание')

        self.btn = QPushButton('Загрузить строки', self)
        self.btn.move(10, 10)

        self.str = QTextBrowser(self)
        self.str.move(10, 50)
        self.str.resize(280, 280)

        self.btn.clicked.connect(self.load_random_string)

    def load_random_string(self):
        with open('lines.txt', encoding='utf8') as f:
            text = f.read().split('\n')
        length = len(text)
        ch = [text[i] for i in range(length) if i % 2 == 0]
        nch = [text[i] for i in range(length) if i % 2 != 0]
        self.str.setText("\n".join(nch) + "\n" + "\n".join(ch))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
