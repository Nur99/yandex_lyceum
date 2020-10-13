import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui2.ui', self)
        self.file_name = None
        self.open.clicked.connect(self.open_f)
        self.save.clicked.connect(self.save_f)
        self.new_2.clicked.connect(self.new_f)

    ## Открываем файл, если нет - создаём
    def open_f(self):
        self.file_name = self.filenameEdit.text()
        if self.file_name and self.file_name in os.listdir():
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(open(self.file_name, 'r', encoding='utf8').read())
        else:
            self.new_f()

    ## Сохраняем файл
    def save_f(self):
        self.file_name = self.filenameEdit.text().strip()
        f = open(self.file_name, 'w', encoding='utf8')
        t = self.plainTextEdit.toPlainText()
        f.write(t)
        f.close()

    ## Создаём новый файл
    def new_f(self):
        self.file_name = self.filenameEdit.text().strip()
        f = open(self.file_name, 'w', encoding='utf8')
        f.write('')
        f.close()
        self.open_f()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
