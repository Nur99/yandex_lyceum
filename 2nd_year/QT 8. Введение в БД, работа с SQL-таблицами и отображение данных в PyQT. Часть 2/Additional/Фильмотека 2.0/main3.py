import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox

DB_NAME = "films_db.sqlite"


class AddFilmWidget(QMainWindow):
    def __init__(self, parent=None, film_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        uic.loadUi('addFilm.ui', self)
        self.selectGenres()
        self.film_id = film_id
        if film_id is not None:
            self.pushButton.clicked.connect(self.edit_elem)
            self.pushButton.setText('Отредактировать')
            self.setWindowTitle('Редактирование записи')
            self.get_elem()

        else:
            self.pushButton.clicked.connect(self.add_elem)

    def get_elem(self):
        cur = self.con.cursor()
        item = cur.execute(
            f"SELECT f.id, f.title, f.year, g.title, f.duration FROM films as f JOIN genres as g ON g.id = f.genre WHERE f.id = {self.film_id}").fetchone()
        self.title.setPlainText(item[1])
        self.year.setPlainText(str(item[2]))
        self.comboBox.setCurrentText(item[3])
        self.duration.setPlainText(str(item[4]))

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
            self.parent().update_films()
            self.close()

    def edit_elem(self):
        cur = self.con.cursor()
        try:
            new_data = (self.title.toPlainText(), int(self.year.toPlainText()),
                        self.params.get(self.comboBox.currentText()), int(self.duration.toPlainText()), self.film_id)
            cur.execute("UPDATE films SET title=?, year=?, genre=?, duration=? WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_films()
            self.close()


class AddGenreWidget(QMainWindow):
    def __init__(self, parent=None, genre_id=None):
        super().__init__(parent)
        self.con = sqlite3.connect(DB_NAME)
        self.params = {}
        uic.loadUi('addGenre.ui', self)
        self.genre_id = genre_id
        if genre_id is not None:
            self.saveButton.clicked.connect(self.edit_elem)
            self.setWindowTitle('Редактирование записи')
            self.get_elem()
        else:
            self.saveButton.clicked.connect(self.add_elem)

    def get_elem(self):
        cur = self.con.cursor()
        item = cur.execute(f"SELECT * FROM genres WHERE id = {self.genre_id}").fetchone()
        self.title.setText(item[1])

    def add_elem(self):
        cur = self.con.cursor()
        try:
            id_off = cur.execute("SELECT max(id) FROM genres").fetchone()[0]
            new_data = (id_off + 1, self.title.text())
            cur.execute("INSERT INTO genres VALUES (?,?)", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_genres()
            self.close()

    def edit_elem(self):
        cur = self.con.cursor()
        try:
            new_data = (self.title.text(), self.genre_id)
            cur.execute("UPDATE genres SET title=? WHERE id=?", new_data)
        except ValueError as ve:
            self.statusBar().showMessage("Неверно заполнена форма")
            print(ve)
        else:
            self.con.commit()
            self.parent().update_genres()
            self.close()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect(DB_NAME)
        self.update_films()
        self.addFilmButton.clicked.connect(self.add_film)
        self.editFilmButton.clicked.connect(self.edit_film)
        self.deleteFilmButton.clicked.connect(self.delete_film)
        self.addGenreButton.clicked.connect(self.add_genre)
        self.editGenreButton.clicked.connect(self.edit_genre)
        self.deleteGenreButton.clicked.connect(self.delete_genre)
        self.dialogs = list()
        self.exitAction.triggered.connect(self.close_app)
        self.tabWidget.currentChanged.connect(self.tab_changed)

    def update_films(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        que = "SELECT f.id, f.title, f.year, g.title, f.duration FROM films as f JOIN genres as g ON g.id = f.genre ORDER BY f.id DESC"
        result = cur.execute(que).fetchall()

        # Заполнили размеры таблицы
        self.filmsTable.setRowCount(len(result))
        self.filmsTable.setColumnCount(len(result[0]))
        self.filmsTable.setHorizontalHeaderLabels(
            ['ИД', 'Название фильма', 'Год выпуска', 'Жанр', 'Продолжительность'])

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.filmsTable.setItem(i, j, QTableWidgetItem(str(val)))

    def update_genres(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        que = "SELECT id, title FROM genres"
        result = cur.execute(que).fetchall()

        # Заполнили размеры таблицы
        self.genresTable.setRowCount(len(result))
        self.genresTable.setColumnCount(len(result[0]))
        self.genresTable.setHorizontalHeaderLabels(
            ['ИД', 'Название жанра'])

        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.genresTable.setItem(i, j, QTableWidgetItem(str(val)))

    def add_film(self):
        dialog = AddFilmWidget(self)
        dialog.show()

    def add_genre(self):
        dialog = AddGenreWidget(self)
        dialog.show()

    def edit_film(self):
        rows = list(set([i.row() for i in self.filmsTable.selectedItems()]))
        ids = [self.filmsTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddFilmWidget(self, film_id=ids[0])
        dialog.show()

    def edit_genre(self):
        rows = list(set([i.row() for i in self.genresTable.selectedItems()]))
        ids = [self.genresTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        dialog = AddGenreWidget(self, genre_id=ids[0])
        dialog.show()

    def delete_film(self):
        rows = list(set([i.row() for i in self.filmsTable.selectedItems()]))
        ids = [self.filmsTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self, '', "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы. Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from films WHERE ID in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_films()

    def delete_genre(self):
        rows = list(set([i.row() for i in self.genresTable.selectedItems()]))
        ids = [self.genresTable.item(i, 0).text() for i in rows]
        if not ids:
            self.statusBar().showMessage('Ничего не выбрано')
            return
        else:
            self.statusBar().showMessage('')
        valid = QMessageBox.question(self, '', "Действительно удалить элементы с id " + ",".join(ids),
                                     QMessageBox.Yes,
                                     QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы. Не забываем зафиксировать изменения
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from genres WHERE id in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_genres()

    def close_app(self):
        self.close()

    def tab_changed(self, index):
        if index == 0:
            self.update_films()
        else:
            self.update_genres()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
