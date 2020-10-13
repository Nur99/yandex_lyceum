import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class FileStat(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('filestat.ui', self)
        self.processButton.clicked.connect(self.min_med_max)

    def min_med_max(self):
        filename = self.filenameEdit.text()
        try:
            with open(filename, 'r', encoding='utf8') as f:
                numbers = list(map(int, f.read().split()))
                min_num, max_num, avg_num = min(numbers), max(numbers), sum(numbers) / len(numbers)
                self.minEdit.setValue(min_num)
                self.maxEdit.setValue(max_num)
                self.avgEdit.setValue(avg_num)

            with open('output.txt', 'w', encoding='utf8') as f:
                f.write(
                    f"Максимальное значение = {max_num}\nСреднее значение = {min_num}\nМинимальное значение = {avg_num}")
        except FileNotFoundError:
            self.statusBar().showMessage(f"Файл '{filename}' не найден")
        except ValueError:
            self.statusBar().showMessage(f"В файле'{filename}' содержатся некорректные данные")

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileStat()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
