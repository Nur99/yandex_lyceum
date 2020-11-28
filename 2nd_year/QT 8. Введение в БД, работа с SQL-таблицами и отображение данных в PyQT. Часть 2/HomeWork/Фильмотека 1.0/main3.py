import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_add import Ui_Form as Ui_add

DB_NAME = "films_db.sqlite"


class AddWidget(QMainWindow, Ui_add):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        self.setupUi(self)
        self.selectGenres()
        self.pushButton.clicked.connect(self.add_elem)

    def selectGenres(self):
        req = "SELECT * from genres"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params[key] = value
        self.comboBox.addItems(list(self.params.keys()))

    def add_elem(self):
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM films").fetchone()[0]
            new_data = (id_off + 1, self.title.toPlainText(), int(self.year.toPlainText()),
                        self.params.get(self.comboBox.currentText()), int(self.duration.toPlainText()))
            cur.execute("INSERT INTO films VALUES (?,?,?,?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_result()
            self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect(DB_NAME)
        self.update_result()
        self.addButton.clicked.connect(self.adding)
        self.dialogs = list()

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        que = "SELECT f.id, f.title, f.year, g.title, f.duration FROM films as f JOIN genres as g ON g.id = f.genre ORDER BY f.id DESC"
        result = cur.execute(que).fetchall()

        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def adding(self):
        dialog = AddWidget(self)
        dialog.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
