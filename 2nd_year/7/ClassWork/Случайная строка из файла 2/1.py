import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QPushButton
import random

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 550, 50)
        self.setWindowTitle('Cлучайная строка')
        self.button = QPushButton("Получить", self)
        self.button.move(10, 10)
        self.button.resize(100, 30)
        self.str = QTextBrowser(self)
        self.str.move(120,10)
        self.str.resize(430,30)
        self.button.clicked.connect(self.load_random_string)



    def load_random_string(self):
        try:
            with open('lines.txt', encoding='utf8') as f:
                text = f.read().split('\n')

            self.str.setText(random.choice(text) if text else "Файл пустой")
        except FileNotFoundError:
            self.str.setText("Файл не найден")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())




